import pandas as pd
import numpy as np 
from nba_api.stats.endpoints import boxscorematchups
import time

df = pd.read_csv('/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/game_odds_combined.csv')
game_list = df['Game_ID'].tolist()
print(game_list)

list = []
for game_id in game_list:
	gamefinder = boxscorematchups.BoxScoreMatchups(game_id= '00'+str(game_id))
	game = gamefinder.get_data_frames()[0]
	print(game_id)
	list.append(game)
	time.sleep(0.5)
matchup_list = pd.concat(list)
matchup_list.to_csv('matchup.csv', index=False)