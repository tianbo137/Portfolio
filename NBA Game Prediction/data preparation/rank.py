import pandas as pd 
import numpy as np
from datetime import datetime


def rename_columns(df):
    df = df.rename(columns={
        'Season': 'SEASON'
    })
#    df.columns = df.columns.str.lower()
    return df

def reorder_columns(df):
    first_cols = [
        'GAME_DATE',
        'Game_ID',
        'TEAM',
        'MATCHUP',
        'WL',
        'PTS'
    ]
    last_cols = [
    	'SEASON',
        'Is_Regular',
        'Team_ID',
        'CONFERENCE',
    ]
    cols = (
        first_cols +
        [col for col in df.columns if col not in (first_cols+last_cols)] +
        last_cols
    )
    return df[cols]



def parse_matchup(df):
    """
    Add more useful columns based upon matchup information.
    """

    df['HV'] = np.where(df['MATCHUP'].str.contains('@'), 'V', 'H')
    df['OPP_TEAM'] = df['MATCHUP'].str.split(' ').str.get(-1)

    # Put new columns where matchup used to be, and drop matchup
    cols = []
    for col in df.columns:
        if col not in ['MATCHUP', 'HV', 'OPP_TEAM']:
            cols.append(col)
        elif col == 'MATCHUP':
            cols.append('HV')
            cols.append('OPP_TEAM')
    return df[cols]

def process_data(df):

	try:
		nba_teams_dict = {'ATL': 1610612737, 'BOS': 1610612738, 'CLE': 1610612739, 'NOP': 1610612740, 'CHI': 1610612741, 'DAL': 1610612742, 'DEN': 1610612743, 'GSW': 1610612744, 'HOU': 1610612745, 'LAC': 1610612746, 'LAL': 1610612747, 'MIA': 1610612748, 'MIL': 1610612749, 'MIN': 1610612750, 'BKN': 1610612751, 'NYK': 1610612752, 'ORL': 1610612753, 'IND': 1610612754, 'PHI': 1610612755, 'PHX': 1610612756, 'POR': 1610612757, 'SAC': 1610612758, 'SAS': 1610612759, 'OKC': 1610612760, 'TOR': 1610612761, 'UTA': 1610612762, 'MEM': 1610612763, 'WAS': 1610612764, 'DET': 1610612765, 'CHA': 1610612766}
		inv_map = {v: k for k, v in nba_teams_dict.items()}

		western_conference = ('DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MEM', 'MIN', 'NOP', 'OKC', 'PHX', 'POR', 'SAC', 'SAS', 'UTA')
		eastern_conference = ('ATL', 'BOS', 'CHA', 'CHI', 'CLE', 'DET', 'IND', 'MIA', 'MIL', 'NYK', 'ORL', 'PHI','TOR', 'WAS', 'BKN')
		
		# Modify the format of datetime in the game_stats table

		df['GAME_DATE'] = df['GAME_DATE'].apply(lambda x: datetime.strptime(x, '%b %d, %Y'))
		df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
		df['TEAM'] = df['Team_ID'].map(inv_map)
		df['CONFERENCE'] = df['TEAM'].apply(lambda x: 'W' if x in western_conference else 'E')
		df.sort_values(by=['GAME_DATE', 'Game_ID'], inplace = True)
		df = rename_columns(df)
		df = reorder_columns(df)
		df = parse_matchup(df)
		df['OPP_CONFERENCE'] = df['OPP_TEAM'].apply(lambda x: 'W' if x in western_conference else 'E')
	except Exception as e:
		print(e)
		print("Team data preparation failed")
	return df

game_stats = pd.read_csv('/Users/btian/Documents/GitHub/portfolio/NBA Game Prediction/data/complete_game_stat.csv')
game_stats = process_data(game_stats)
game_stats.to_csv('/Users/btian/Documents/GitHub/portfolio/NBA Game Prediction/data/processed_game_stat.csv')