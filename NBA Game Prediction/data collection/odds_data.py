import pandas as pd
from datetime import datetime

seasons = ['2014-15', '2015-16', '2016-17', '2018-19', '2019-20', '2020-21']

list = []
for season in seasons:
	df = pd.read_excel('nba odds '+ season + '.xlsx')
	df['Season'] = season
	list.append(df)
df = pd.concat(list)
df.to_csv('odds_data.csv', index=False)

df = pd.read_csv('odds_data.csv')
print(df.head(6))