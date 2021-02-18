import pandas as pd
import numpy as np
import time
from pathlib import Path


from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import boxscoreplayertrackv2
from nba_api.stats.endpoints import boxscoreadvancedv2


df = pd.read_csv('complete_game_stat.csv')

game_id = df['Game_ID'].tolist()
reduced_game_id = [] 
for i in game_id: 
    if i not in reduced_game_id: 
    	reduced_game_id.append(i)

print(len(reduced_game_id))
#def listComplementElements(list1, list2):
#	storeResults = []
#	for num in list1:
#		if num not in list2:
#			storeResults.append(num)
#	return storeResults

#result = listComplementElements(reduced_game_id, b)
for id in reduced_game_id:
	my_file = Path("/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/"+ str(id) + "_game_stat.csv")
	print(my_file)
	if my_file.is_file():
		pass
	else:
		game_data = boxscoreplayertrackv2.BoxScorePlayerTrackV2(game_id="00"+str(id))
		df1 = game_data.get_data_frames()[0]
		time.sleep(0.2)
		ad_game_data = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id="00"+str(id))
		df2 = ad_game_data.get_data_frames()[0]
		df = pd.merge(df1, df2,  how='left', left_on=['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN'], right_on = ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN'])
		df.to_csv(str(id)+'_game_stat.csv', index=False)
		time.sleep(0.2)

data_list = []
for id in reduced_game_id:
	my_file = Path("/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/"+ str(id) + "_game_stat.csv")
	print(my_file)
	df = pd.read_csv(my_file)
	data_list.append(df)
complete_player_game_stat = pd.concat(data_list)
complete_player_game_stat.to_csv('complete_player_game_stat.csv', index=False)

