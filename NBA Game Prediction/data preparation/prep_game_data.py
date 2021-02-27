import numpy as np
import pandas as pd



def prep_team_data(df):

    '''
    Cleans match result data
    param df: Dataframe of raw match results
    return: DataFrame of clean match results
    '''

    nba_teams_dict = {'ATL': 1610612737, 'BOS': 1610612738, 'CLE': 1610612739, 'NOP': 1610612740, 'CHI': 1610612741, 'DAL': 1610612742, 'DEN': 1610612743, 'GSW': 1610612744, 'HOU': 1610612745, 'LAC': 1610612746, 'LAL': 1610612747, 'MIA': 1610612748, 'MIL': 1610612749, 'MIN': 1610612750, 'BKN': 1610612751, 'NYK': 1610612752, 'ORL': 1610612753, 'IND': 1610612754, 'PHI': 1610612755, 'PHX': 1610612756, 'POR': 1610612757, 'SAC': 1610612758, 'SAS': 1610612759, 'OKC': 1610612760, 'TOR': 1610612761, 'UTA': 1610612762, 'MEM': 1610612763, 'WAS': 1610612764, 'DET': 1610612765, 'CHA': 1610612766}
	inv_map = {v: k for k, v in nba_teams_dict.items()}
	western_conference = ('DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MEM', 'MIN', 'NOP', 'OKC', 'PHX', 'POR', 'SAC', 'SAS', 'UTA')
	eastern_conference = ('ATL', 'BOS', 'CHA', 'CHI', 'CLE', 'DET', 'IND', 'MIA', 'MIL', 'NYK', 'ORL', 'PHI','TOR', 'WAS', 'BKN')
	
	try:
		# Modify the format of datetime in the game_stats table
		df['GAME_DATE'] = df['GAME_DATE'].apply(lambda x: datetime.strptime(x, '%b %d, %Y'))
		df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
		df['Team'] = df['Team_ID'].map(inv_map)
		df['CONFERENCE'] = df['Team'].apply(lambda x: 'W' if x in western_conference else 'E')
		df.sort_values(by=['GAME_DATE', 'Game_ID'], inplace = True)

        # Clean opposition field
        df['Opposition'] = df['Opposition'].str.split(" ", n=1, expand=True)[1]

        # Ensure team and opposition names match
        u = {'United States of America': 'USA'}
        df['Team'] = df['Team'].map(u).fillna(df['Team'])

        # Remove one copy of each result
        df = df.drop_duplicates(subset=['Result', 'For', 'Aga', 'Diff', 'Ground', 'Match Date'], keep='first')

        # Take only wins and draws to remove duplicates
        df = df[df.Result != 'lost']

        # Remove rows where opposition is blank
        df['Opposition'].replace('', np.nan, inplace=True)
        df = df.dropna(subset=['Opposition'])

        # Remove rows where games havent been played yet
        df['Result'].replace('-', np.nan, inplace=True)
        df.dropna(subset=['Result'], inplace=True)

        # Only use countries from list
        df = df[df['Team'].isin(country) & df['Opposition'].isin(country)]

        df['Match Date'] = pd.to_datetime(df['Match Date']).dt.date




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


def add_rankings(match_results_clean, rankings):

    '''
    Adds WR rankings to match results
    :param match_results_clean: DataFrame of clean match results
    :param rankings: DataFrame of WR rankings
    :return: A DataFrame of combined match results and their associated team WR rankings
    '''

    # Ensure Match Date format is the same between team_ratings and all_rankings
    rankings['Match Date']=rankings['Match Date'].apply(lambda x : pd.to_datetime(x, format = '%d/%m/%Y'))
    match_results_clean['Match Date'] = pd.to_datetime(match_results_clean['Match Date'], format='%Y/%m/%d')

    # Merge team and opposition rankings
    match_results_rankings = pd.merge(match_results_clean,rankings, left_on=['Team','Match Date'],
                                      right_on=['Team','Match Date'], how='left')

    match_results_rankings.drop_duplicates(inplace=True)
    match_results_rankings = pd.merge(match_results_rankings,rankings, left_on=['Opposition','Match Date'],
                                      right_on=['Team','Match Date'], how='left')

    match_results_rankings.rename({"pts_x":'Team ranking pts',"pts_y":'Opposition ranking pts',"Team_x":'Team'},
                                  axis=1, inplace=True)
    match_results_rankings.drop_duplicates(subset=['Team', 'Opposition', 'Match Date'], inplace=True)

    match_results_rankings = match_results_rankings[['Team', 'Result','For','Aga','Diff',
                                                     'Opposition','Match Date','Team ranking pts',
                                                     'Opposition ranking pts']]

    # World Rugby rankings started in Oct 2003 so remove blank rows / matches before Oct 2003
    match_results_rankings.dropna(subset=['Team ranking pts'], inplace=True)

    return match_results_rankings




def get_stats(df, country):

    '''
    Get latest rankings and skills as at last played match
    :param df: DataFrame of latest match results, WR rankings and skill levels
    :param country: List of countries to include
    :return: DataFrame of latest ranking and skill level by team
    '''


    df = df.sort_values(['Match Date'], ascending=True)
    stats = pd.DataFrame()
    for i in country:
        tmp = (df.loc[(df['Team'] == i)].tail(1))
        stats = pd.concat([stats,tmp])

    return stats[['Team','Match Date','Team ranking pts',
                  'Team skill','Team sigma']]

conn = sqlite3.connect('match_results.db')
cursor = conn.cursor()

country = ['New Zealand', 'South Africa', 'England', 'Wales',
           'Scotland', 'Australia', 'France', 'Argentina',
           'Ireland', 'Fiji', 'Italy', 'Samoa', 'Japan',
           'Canada', 'Tonga', 'USA',
           'Georgia', 'Russia', 'Romania']

# Clean match result data
try:
    raw_data = pd.read_sql_query('SELECT * from raw_data',conn)
    match_results_clean = prep_team_data(raw_data, country)
    print('Team data prepared')

except Exception as e:
    print(e)
    print("Failed on match result data prep")

# Add World Rugby Rankings
try:
    rankings = pd.read_sql_query('SELECT * from rankings', conn)
    match_results_clean = match_results_clean.drop_duplicates(subset=['Team', 'Result','For','Aga','Diff','HTf',
                                                                      'HTa','Opposition','Ground','Match Date'])

    match_results_with_rankings = add_rankings(match_results_clean, rankings)
    # match_results_with_rankings.to_sql('match_results_with_rankings', conn, if_exists='replace')
    print("World Rugby rankings added")

except Exception as e:
    print(e)
    print("Failed adding World Rugby Rankings")

# Calculate team skill levels
try:
    matches_rankings_skill = skill_level.rate_teams(match_results_with_rankings)
    print("Team skill assessment complete")

except Exception as e:
    print(e)
    print("Failed on team skill level")

# Add in lost results for model
try:
    data_for_model = add_lost_results(matches_rankings_skill)
    # data_for_model.to_csv('model_training_data.csv')
    matches_rankings_skill.to_sql('model_training_data', conn, if_exists='replace')
    print("Lost results added back to data")
    print("Model training data prepared")

except Exception as e:
    print(e)
    print("Failed at model data preparation")

# Get latest rankings and skills as at last played match
try:
    latest_stats = get_stats(data_for_model, country)
    latest_stats.to_sql('latest_stats', conn, if_exists='replace')
except Exception as e:
    print(e)
    print("Failed retrieving latest team stats")


game_stats = pd.read_csv('/Users/btian/Documents/GitHub/My_Data_Portfolio/NBA Game Prediction/data/complete_game_stat.csv')



