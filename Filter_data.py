'''
In our data file all_matches.csv we have all the international matches from 1872 to 2026 up to date but first 
we filter out the only the recent matches. We are going to consider only the matches bettween Jan 2023 and June 2026 for 
this wc probability code.
'''

import pandas as pd

start_date = '2023-01-01'
end_date = '2026-06-01'

d = pd.read_csv(r'C:\Users\anath\OneDrive\Desktop\Projects\Probabiltiy\results.csv')

filter = (d['date'] >= start_date) & (d['date'] <= end_date)

nd = d.loc[filter]
#nd.to_csv('recent_data.csv',index = False)

qualified_teams = [
    "Mexico","South Africa","South Korea","Czech Republic",
    "Canada","Bosnia and Herzegovina","Qatar","Switzerland",
    "Brazil","Morocco","Haiti","Scotland",
    "United States","Paraguay","Australia","Turkey",
    "Germany","Curaçao","Ivory Coast","Ecuador",
    "Netherlands","Japan","Sweden","Tunisia",
    "Belgium","Egypt","Iran","New Zealand",
    "Spain","Cape Verde","Saudi Arabia","Uruguay",
    "France","Senegal","Iraq","Norway",
    "Argentina","Algeria","Austria","Jordan",
    "Portugal","DR Congo","Uzbekistan","Colombia",
    "England","Croatia","Ghana","Panama",
]

'''
Now we will only consider the matches of World Cup Teams.
We will create a new csv file where only the 48 world cup teams will be listed along with their matches played 
and number of wins.
'''
nd = pd.read_csv(r'C:\Users\anath\OneDrive\Desktop\Projects\Probabiltiy\recent_data.csv')

filter_wc = (nd['home_team'].isin(qualified_teams)) & (nd['away_team'].isin( qualified_teams))

wc_d = nd.loc[filter_wc]
#wc_d.to_csv('WC_data.csv',index = False)

'''
We have now created a file with only the matches of the teams participating in the world cup.
Now We make aa new csv file for our final work which will contain each team name along with the datas mentioned 
in the headers list below.
'''

headers = [
'team_name', 
'matches_played', 
'matches_won', 
'matches_lost', 
'matches_tied', 
'win_percentage', 
'loss_percentage', 
'tie_percentage',
'total_goals',
'goals_per_match'
]

'''
We first create an empty data frame and then step by step add the data of the teams from our Wc_data file
'''
empty_data = pd.DataFrame(columns=headers)

WC_D = pd.read_csv(r'C:\Users\anath\OneDrive\Desktop\Projects\Probabiltiy\WC_data.csv')

# We uniquely identify the teams in the next line and then sort them
'''
Unique_teams = set(WC_D['home_team']).union(set(WC_D['away_team']))
sorted_teams = sorted(list(Unique_teams))
'''

sorted_teams = sorted(qualified_teams)

#We put this teams now into the csv file for final data
empty_data['team_name'] = sorted_teams
empty_data['team_name'] = sorted_teams

#Now we count the total number of matches played by each team and then add them
home_counts = WC_D['home_team'].value_counts()
away_counts = WC_D['away_team'].value_counts()
total_matches = home_counts.add(away_counts, fill_value=0) # fill value=0 ensures that even if a team has played only home matches the code does'nt break

# Now we map these totals back to the empty_data rows matching the 'team_name'
# .map() fucntion looks at the team_name and matches it with  their corresponding total from total_matches
# We now map the data into the file and save it
empty_data['matches_played'] = empty_data['team_name'].map(total_matches).fillna(0).astype(int)

# Now we will count how many matches is won and lost by each team, firstly we set the default value to draw
WC_D['winner'] = 'Draw' 
WC_D['loser'] = 'Draw'

#We check the score of each home team and away team to decide  win/loss/draw.

#Wins

WC_D.loc[WC_D['home_score'] > WC_D['away_score'], 'winner'] = WC_D['home_team']
WC_D.loc[WC_D['away_score'] > WC_D['home_score'], 'winner'] = WC_D['away_team']

#Loss

WC_D.loc[WC_D['home_score'] < WC_D['away_score'], 'loser'] = WC_D['home_team']
WC_D.loc[WC_D['away_score'] < WC_D['home_score'], 'loser'] = WC_D['away_team']

#Draw

draw_matches = WC_D[WC_D['home_score'] == WC_D['away_score']]
#This counts how many times each team appeared in a draw each time as a home and away team
home_draw_counts = draw_matches['home_team'].value_counts()
away_draw_counts = draw_matches['away_team'].value_counts()

#We then count how many times each team shows up as a winner and loser and draw
win_counts = WC_D['winner'].value_counts()
loss_counts = WC_D['loser'].value_counts()
total_ties = home_draw_counts.add(away_draw_counts, fill_value=0)

#again mapping them back and saving it to the csv file
empty_data['matches_lost'] = empty_data['team_name'].map(loss_counts).fillna(0).astype(int)
empty_data['matches_won'] = empty_data['team_name'].map(win_counts).fillna(0).astype(int)
empty_data['matches_tied'] = empty_data['team_name'].map(total_ties).fillna(0).astype(int)

'''
Now, in this part of the code we will calculate the win , loss and tie percentage of each of the teams respectively.
'''

#Win Percentage rounded off to 4 decimal places
empty_data['win_percentage'] = (
(empty_data['matches_won'] / empty_data['matches_played'] * 100)
.where(empty_data['matches_played'] > 0, 0)
.round(2)
)

#Loss Percentage rounded off to 4 decimal places
empty_data['loss_percentage'] = (
    (empty_data['matches_lost'] / empty_data['matches_played'] * 100)
    .where(empty_data['matches_played'] > 0, 0)
    .round(2)
)

#Tie Percentage rounded off to 4 decimal places
empty_data['tie_percentage'] = (
    (empty_data['matches_tied'] / empty_data['matches_played'] * 100)
    .where(empty_data['matches_played'] > 0, 0)
    .round(2)
)

#Now we will add the total goals scored and goals per match to have a basic understanding of the agreesiveness of the team
#Firstly we'll count the total goals scored by team in both home and away matches
home_goals = WC_D.groupby('home_team')['home_score'].sum()
away_goals = WC_D.groupby('away_team')['away_score'].sum()
#Now we use this data to calculate the total goals
total_goals = home_goals.add(away_goals, fill_value=0)

#adding the total goals in the data

empty_data['total_goals'] = empty_data['team_name'].map(total_goals).fillna(0).astype(int)

#Goals Per Match
empty_data['goals_per_match'] = (
    (empty_data['total_goals'] / empty_data['matches_played'])
    .where(empty_data['matches_played'] > 0, 0)
    .round(2)
)

#SAVING the final data
empty_data.to_csv('World Cup Final Data', index = False)

'''
All the calculations done are to make sure zero division error is avoided and decimal points upto 2 places are considered.
Many portions of this code can be shortened to make the code more compact, but as i myself am a beginner
I have shown all the basic step by step analysis for my own understanding.
'''


