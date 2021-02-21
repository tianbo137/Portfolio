import numpy as np
import pandas as pd

games = pd.read_csv('/Users/btian/Documents/GitHub/portfolio/NBA Game Prediction/data/processed_game_stat.csv')

games.set_index('Game_ID')

home_games = games[games['HV'] == 'H']
print(home_games.head())

away_games = games[games['HV'] == 'V']
print(away_games.head())

df = home_games.join(away_games, lsuffix='_H', rsuffix='_V').head()
print(df)