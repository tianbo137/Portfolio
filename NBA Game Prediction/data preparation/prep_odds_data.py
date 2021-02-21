import pandas as pd
import numpy as np
from nba_api.stats import endpoints
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
import time
from datetime import datetime



def prep_odds_data(df):

    

# Change the team name to standard abbreviation
    team_abbr_dict = {'Dallas': 'DAL', 
                      'SanAntonio': 'SAS',  
                      'Orlando': 'ORL', 
                      'NewOrleans': 'NOP', 
                      'Houston':'HOU', 
                      'LALakers':'LAL',
                      'Milwaukee': 'MIL', 
                      'Charlotte':'CHA', 
                      'Philadelphia':'PHI',
                      'Indiana':'IND', 
                      'Brooklyn':'BKN', 
                      'Boston':'BOS',
 	                  'Atlanta':'ATL', 
 	      	          'Toronto':'TOR', 
 	                  'Washington':'WAS', 
 		              'Miami':'MIA', 
 		              'Chicago':'CHI', 
 		              'NewYork':'NYK', 
 		              'Minnesota':'MIN',
 		              'Memphis':'MEM', 
 		              'Detroit':'DET', 
 		              'Denver':'DEN', 
 		              'Utah':'UTA', 
 		              'Phoenix':'PHX', 
 		              'GoldenState':'GSW', 
 		              'Sacramento':'SAC',
 		              'OklahomaCity':'OKC',
 	                  'Portland':'POR', 
 	                  'Cleveland':'CLE', 
 	                  'LAClippers':'LAC',
 	                  'Oklahoma City':'OKC', 
 	                  'LA Clippers':'LAC'}
    df['Team'] = df['Team'].map(team_abbr_dict)
    df = df.astype({"Date":'str'}) 

# Change team name to team id
    team_id_dict = {'ATL': 1610612737, 
                      'BOS': 1610612738, 
                      'CLE': 1610612739, 
                      'NOP': 1610612740, 
                      'CHI': 1610612741, 
                      'DAL': 1610612742, 
                      'DEN': 1610612743, 
                      'GSW': 1610612744, 
                      'HOU': 1610612745, 
                      'LAC': 1610612746, 
                      'LAL': 1610612747, 
                      'MIA': 1610612748, 
                      'MIL': 1610612749, 
                      'MIN': 1610612750, 
                      'BKN': 1610612751, 
                      'NYK': 1610612752, 
                      'ORL': 1610612753, 
                      'IND': 1610612754, 
                      'PHI': 1610612755, 
                      'PHX': 1610612756, 
                      'POR': 1610612757, 
                      'SAC': 1610612758, 
                      'SAS': 1610612759, 
                      'OKC': 1610612760, 
                      'TOR': 1610612761, 
                      'UTA': 1610612762, 
                      'MEM': 1610612763, 
                      'WAS': 1610612764, 
                      'DET': 1610612765, 
                      'CHA': 1610612766}

    df['Team_ID'] = df['Team'].map(team_id_dict).astype('int64')
    
    # Add game datetime to the odds table

    df['Month'] = df.apply(lambda x: game_month(x['Date']), axis=1)
    df['Day'] = df.apply(lambda x: game_day(x['Date']), axis=1)
    df['Year'] = df.apply(lambda x: game_year(x['Month'], x['Season']), axis=1)
    df['GAME_DATE'] = df['Year'] + "-" + df['Month'] + "-" + df['Day']
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'], format='%Y-%m-%d')
     
    # Restrict to season after 2014-2015
    df = df[df['Season'] != '2014-15']


    df = df[['GAME_DATE', 'Season', 'Team', 'Team_ID', 'VH', '1st', '2nd', '3rd', '4th', 'Final', 'ML']]

    df = df.rename(columns={'Season': 'SEASON','Team': 'TEAM'})

    return df


def game_month(date):
    return date[0:2] if len(date) == 4 else date[0:1]

def game_day(date):
	return date[2:4] if len(date) == 4 else date[1:3]   

def game_year(month, season):
    return season[0:4] if int(month) >= 10 else '20'+ season[-2:]




odds = pd.read_csv('/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/odds_data.csv')
processed_odds = prep_odds_data(odds)
processed_odds.to_csv (r'/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/processed_odds_data.csv', index = False, header=True)

