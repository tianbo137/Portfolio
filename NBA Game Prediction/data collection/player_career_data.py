import pandas as pd
import numpy as np
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
d = [player for player in nba_players if player['is_active'] == True]
nba_active_players = pd.DataFrame(d)

# Remove columns name   'is_active' 
nba_active_players.drop(['is_active'], axis = 1, inplace=True) 
print('Number of active players fetched: {}'.format(len(nba_active_players)))
nba_active_players.to_csv('nba_active_players.csv', index=False)

player_id = nba_active_players['id'].tolist()
player_info = []
for id in player_id:
    career = playercareerstats.PlayerCareerStats(player_id=id)
    print(id)
    id_info = career.get_data_frames()[0]
    player_info.append(id_info)
    time.sleep(1)
# see pd.concat documentation for more info
df = pd.concat(player_info)
df.to_csv('player_career_stats.csv', index=False)
