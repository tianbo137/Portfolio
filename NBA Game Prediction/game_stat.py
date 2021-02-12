import pandas as pd
import numpy as np

import requests
from selenium import webdriver
import re
import time



pd.set_option('display.max_columns', 30)


# Create list of seasons to look at
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21']


# Scrapes stats.nba.com to get season average statistics using Selenium, creates Pandas dataframe from statistics, and concatenates each year's dataframe with the prior year
def get_data(seasons_list):
    statistics = pd.DataFrame()
    for season in seasons_list:
        url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=' + season + '&SeasonType=Regular%20Season'
        driver = webdriver.Chrome(r"/Users/btian/Downloads/")
        driver.get(url)
        time.sleep(3)
        table = driver.find_element_by_class_name('nba-stat-table__overflow')
        remove_endline = table.text.split('\n')
        row_to_string = ' '.join(remove_endline)
        split_lines = re.sub(r'\s\d{1,2}\s([A-Z])', r'\n\1', row_to_string)
        separate_teams = split_lines.split('\n')
        table_list = []
        for row in separate_teams:
            split_stats = row.split()
            table_list.append(split_stats[-27:])
        df = pd.DataFrame.from_records(table_list[1:], columns = table_list[0])
        df.insert(0, 'SEASON', season)
        statistics = pd.concat([statistics, df], ignore_index = True)
        driver.close()
    return statistics

statistics_df = get_data(seasons)
statistics_df

# Save large dataframe to file for use in analysis
statistics_df.to_csv('nba_statistics_pergame.csv', index=False)