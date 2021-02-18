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

data_list = []
for id in reduced_game_id:
	my_file = Path("/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/"+ str(id) + "_game_stat.csv")
	print(my_file)
	df = pd.read_csv(my_file)
	data_list.append(df)
complete_player_game_stat = pd.concat(data_list)
complete_player_game_stat.to_csv('complete_player_game_stat.csv', index=False)

