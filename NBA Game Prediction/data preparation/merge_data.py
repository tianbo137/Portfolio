import pandas as pd 
import numpy as numpy
from datetime import datetime


#print(game_stats)

processed_odds = pd.read_csv('/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/processed_odds_data.csv')



combined_df = pd.merge(game_stats, processed_odds, how='inner', left_on=['GAME_DATE','Team', 'Season', 'Team_ID'], right_on = ['GAME_DATE','Team', 'Season', 'Team_ID'])
combined_df.sort_values(by='GAME_DATE', inplace = True)
print(combined_df.info())
col = ['Team_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'W', 'L', 'W_PCT',
       'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
       'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
       'PTS', 'Season', 'Is_Regular', 'Team', 'VH', '1st', '2nd', '3rd', '4th',
       'Final', 'ML']

data_path=r'/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/'
combined_df.to_csv(data_path+'game_odds_combined.csv', index=False)


def rename_raw_columns(df):
    df = df.rename(columns={
        'Season': 'SEASON',
        'Team': 'TEAM'
    })
    return df
combined_df = rename_raw_columns(combined_df)
print(combined_df.columns)


def reorder_raw_columns(df):
    first_cols = [
        'SEASON',
        'GAME_DATE',
        'TEAM',
        'CONFERENCE',
        'MATCHUP',
        'WL',
        'PTS'
    ]
    last_cols = [
        'Game_ID',
        'Team_ID',
    ]
    cols = (
        first_cols +
        [col for col in df.columns if col not in (first_cols+last_cols)] +
        last_cols
    )
    return df[cols]

def prep_game_data(df):
	try:
		df = rename_raw_columns(df)
		df = reorder_raw_columns(df)
	except Exception as e:
		print(e)
		print('Raw Data Preparation Failed!')
	return df

combined_df = prep_game_data(combined_df)
print(combined_df.columns)


