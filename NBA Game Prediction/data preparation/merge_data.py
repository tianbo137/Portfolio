import pandas as pd 
import numpy as numpy
from datetime import datetime

nba_teams_dict = {'ATL': 1610612737, 'BOS': 1610612738, 'CLE': 1610612739, 'NOP': 1610612740, 'CHI': 1610612741, 'DAL': 1610612742, 'DEN': 1610612743, 'GSW': 1610612744, 'HOU': 1610612745, 'LAC': 1610612746, 'LAL': 1610612747, 'MIA': 1610612748, 'MIL': 1610612749, 'MIN': 1610612750, 'BKN': 1610612751, 'NYK': 1610612752, 'ORL': 1610612753, 'IND': 1610612754, 'PHI': 1610612755, 'PHX': 1610612756, 'POR': 1610612757, 'SAC': 1610612758, 'SAS': 1610612759, 'OKC': 1610612760, 'TOR': 1610612761, 'UTA': 1610612762, 'MEM': 1610612763, 'WAS': 1610612764, 'DET': 1610612765, 'CHA': 1610612766}
inv_map = {v: k for k, v in nba_teams_dict.items()}

western_conference = ('DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MEM', 'MIN', 'NOP', 'OKC', 'PHX', 'POR', 'SAC', 'SAS', 'UTA')
eastern_conference = ('ATL', 'BOS', 'CHA', 'CHI', 'CLE', 'DET', 'IND', 'MIA', 'MIL', 'NYK', 'ORL', 'PHI','TOR', 'WAS', 'BKN')

# Modify the format of datetime in the game_stats table
game_stats = pd.read_csv('/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/complete_game_stat.csv')
game_stats['GAME_DATE'] = game_stats['GAME_DATE'].apply(lambda x: datetime.strptime(x, '%b %d, %Y'))
game_stats['GAME_DATE'] = pd.to_datetime(game_stats['GAME_DATE'])
game_stats['Team'] = game_stats['Team_ID'].map(inv_map)
game_stats['CONFERENCE'] = game_stats['Team'].apply(lambda x: 'W' if x in western_conference else 'E')
game_stats.sort_values(by=['GAME_DATE', 'Game_ID'], inplace = True)
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


