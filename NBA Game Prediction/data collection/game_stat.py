import pandas as pd
import numpy as np
from nba_api.stats import endpoints
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
import time

# Headers for my google chrome explorer
headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# Get the list of teams together with their abbreviations
teams = teams.get_teams()
print('Number of teams fetched: {}'.format(len(teams)))
teams = pd.DataFrame.from_dict(teams)
nba_teams = teams[['id','full_name','abbreviation']]
print(nba_teams)

# We will be using the past 6 seasons as training and testing data
seasons = ['2015-16','2016-17','2017-18','2018-19','2019-20', '2020-21']

for team_id in nba_teams['id']:
	appended_data = []
	for season in seasons:
		temp1 = teamgamelog.TeamGameLog(season_type_all_star='Regular Season',team_id=team_id, season=season, headers=headers)
		df1 = temp1.get_data_frames()[0]
		df1['Season'] = season
		df1['Is_Regular'] = 1
		time.sleep(2)
		appended_data.append(df1)
		temp2 = teamgamelog.TeamGameLog(season_type_all_star='Playoffs',team_id=team_id, season=season, headers=headers)
		df2 = temp2.get_data_frames()[0]
		df2['Season'] = season
		df2['Is_Regular'] = 0
		time.sleep(2)
		if len(df2) > 0:
			appended_data.append(df2)
	# see pd.concat documentation for more info
	df = pd.concat(appended_data)
	names = nba_teams[nba_teams['id'] == team_id]['abbreviation']
	for name in names:
		print(name)
	file_name=str(name + "_game")
	df.to_csv(file_name+'.csv', index=False)
	time.sleep(1)


names = teams['abbreviation'].tolist()
data_list = []
for name in names:
	print(name)
	file_name=str(name + "_game")
	df = pd.read_csv(file_name+'.csv')
	data_list.append(df)
complete_game_stat = pd.concat(data_list)
complete_game_stat.to_csv('complete_game_stat.csv', index=False)