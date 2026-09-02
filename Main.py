import pandas as pd
import itertools as itr
import random


'''
First we use a dictionary to define the groups
and then we define the matches and input the point distribution system 
that is,win = +3;loss=+0;Draw=+1:
'''

world_cup_groups = {
    
    'Group A': ["Mexico", "South Africa", "South Korea", "Czech Republic"],
    'Group B': ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
    'Group C': ["Brazil", "Morocco", "Haiti", "Scotland"],
    'Group D': ["United States", "Paraguay", "Australia", "Turkey"],
    'Group E': ["Germany", "Curaçao", "Ivory Coast", "Ecuador"],
    'Group F': ["Netherlands","Japan","Sweden","Tunisia"],
    'Group G': ["Belgium","Egypt","Iran","New Zealand"],
    'Group H': ["Spain","Cape Verde","Saudi Arabia","Uruguay"],
    'Group I': ["France","Senegal","Iraq","Norway"],
    'Group J': ["Argentina","Algeria","Austria","Jordan"],
    'Group K': ["Portugal","DR Congo","Uzbekistan","Colombia"],
    'Group L': ["England","Croatia","Ghana","Panama"],

}

# The points for each match in group stage are defined below.
win_point = 3
loss_point = 0
tie_point = 1

#Initializing each team's initial score to zero by using a dictionary
team_score = {}

for group_name, team_list in world_cup_groups.items():
    for team in team_list:
        team_score[team] = 0


'''
In this next part of the code we are going to see each of the group fixtures
and print them.
To do so we first define an empty dictionary which will store all the group stage fixtures.
'''

group_stage_matches = {}

'''
Next we are going to use itertools.combination() in order to generate all the unique matches and print them 
by running each group through the loop
'''

for group_name, team_list in world_cup_groups.items():
    #itertools.combination() will generate all the unique pairings between the 4 teams in each group
    unique_pairs = list(itr.combinations(team_list,2))
    #Next we will store each pairing in the dictionary created
    group_stage_matches[group_name] = unique_pairs 

    '''    
    The next part  is to print out the group fixtures and see if everything worked well, the next part will be commented as we do not
    necessarily need to print them but instead just store the matches in the above created dictionary
    
    print(f"--- {group_name} Schedule ---")
    for match_num, match in enumerate(unique_pairs, 1):
        print(f" Match {match_num}: {match[0]} vs {match[1]}")
    print() # adds a space between the respective group fixtures

   THE ABOVE PART OF THE CODE CAN BE USED TO PRINT THE MATCHES OF EACH GROUP    
    '''


'''
We will define the latest FIFA Rankings for multiplier purposes.
Explanation: Let us consider a scenario where Argentina has played 4 matches against brazil, france , portugal and germany 
and they won 2 and lost 2 with a 50% win percentage...Similarly say Spain has played 4 matches against Curacao, South Africa, Iran and Panama and
they also won 2 and lost 2 with 50% win percentage...Mathematically Spain and Argentina seem to be equal but in reality Argentina's 
opponent's were lot harder than spain's so argentina is better in reality ...to handle this problem we'll use the multiplier system which
will give bonus for teams playing against harder teams...
To do this multiplayer we will use the latest FIFA Rankings and divide the teams into 4 tiers...

Tier-1 Top 10 teams
Tier-2 10-30 ranked teams
Tier 3 30-50 ranked teams
Tier 4 50 above

Based on this 1.50x , 1.25 x , 1.00 x and 0.75 x multipliers will be provided to teams in tier 1,2,3,4 respectively. 
'''


#FIFA RANKINGS FOR 48 TEAMS IN FIFA WORLD CUP 2026
fifa_rankings = {
    "France": 1,
    "Spain": 2,
    "Argentina": 3,
    "England": 4,
    "Portugal": 5,
    "Brazil": 6,
    "Netherlands": 7,
    "Morocco": 8,
    "Belgium": 9,
    "Germany": 10,
    "Croatia": 11,
    "Colombia": 13,
    "Senegal": 14,
    "Mexico": 15,
    "United States": 16,
    "Uruguay": 17,
    "Japan": 18,
    "Switzerland": 19,
    "Iran": 21,
    "Turkey": 22,
    "Ecuador": 23,
    "Austria": 24,
    "South Korea": 25,
    "Australia": 27,
    "Algeria": 28,
    "Egypt": 29,
    "Canada": 30,
    "Norway": 31,
    "Panama": 33,
    "Ivory Coast": 34,
    "Sweden": 38,
    "Paraguay": 40,
    "Czech Republic": 41,
    "Scotland": 43,
    "Tunisia": 44,
    "DR Congo": 46,
    "Qatar": 55,
    "Iraq": 57,
    "South Africa": 60,
    "Saudi Arabia": 61,
    "Jordan": 63,
    "Bosnia and Herzegovina": 65,
    "Cape Verde": 69,
    "Ghana": 74,
    "Curaçao": 82,
    "Haiti": 83,
    "New Zealand": 85,
    "Uzbekistan": 50
}

'''
This next part of the code , we will now based on the win and loss percentage of each team over the years
will decide that which team may win/loss or the match will be tied...
Scenario: Team A vs Team B
Win A = Win% of A + Loss% of B  <---- This shows how vulnerable is team B against team A
Win B = Win% of B + Loss% of A  <---- This shows how vulnerable is team A against team B
Tie  = Tie% of A + Tie% of B  <---- This shows the chances of draw
'''

#First we extract each teams win, loss and tie percentage from the csv data file we created earleir.

df = pd.read_csv(r'C:\Users\anath\OneDrive\Desktop\Projects\Probability\World Cup Final Data')

#We will store them to a dictionary
team_stats = {}

#Using the loop to extract each team's data...
for index, row in df.iterrows():
    
    t_name   = row['team_name']
    win_pct  = float(row['win_percentage'])
    loss_pct = float(row['loss_percentage'])
    tie_pct  = float(row['tie_percentage'])
    goals_match = float(row['goals_per_match'])
    #Storing the extracted data in the dictionary we defined earlier....
    team_stats[t_name] = [win_pct, loss_pct, tie_pct,goals_match]

'''
Sample data printed for checking...
print(f"Sample data  Mexico: {team_stats.get('Mexico')}")
print(f"Sample data Argentina: {team_stats.get('Argentina')}")
'''

#Firstly, we define the multipliers wrt to the fifa rankings of the teams, we will use a function in this case.
def get_multiplier(team_name):
    
    rank = fifa_rankings.get(team_name, 55) # the 55 interger value is to make sure the code doesnt run into an error 
    #and if it encounter a team which is not in the list it assumes it to be in the undergod category of tier 4.

    if rank <= 10:
        return 1.50
    elif rank <= 30:
        return 1.25
    elif rank <= 50:
        return 1.00
    else:
        return 0.75
    
#Later for the round of 16 and quaterfinals we will be using reduced multipliers
def get_multiplier_knockouts(team_name):
    
    rank_knockouts = fifa_rankings.get(team_name)

    if rank_knockouts <= 10:
        return 1.20
    elif rank_knockouts <= 30:
        return 1.15
    elif rank_knockouts <= 50:
        return 1.10
    else:
        return 1.00


#NOTE: NO MULTIPLIER WILL BE USED FOR SEMIS AND FINALS

'''
The above fuction  checks the FIFA Ranking of the team and gives the multiplier based on its Tier
Tier 1 (1-10): 1.50x ; Tier 2 (11-30): 1.25x ; Tier 3 (31-50): 1.00x ; Tier 4 (51+): 0.75x

For Round of 16 and Quater-Finals
Tier 1 (1-10): 1.20x ; Tier 2 (11-30): 1.15x ; Tier 3 (31-50): 1.10x ; Tier 4 (51+): 1.00x

The next part loops through every matches and assigns a team a and team b to each team playing the match and then
applies the multiplier by looking at the FIFA Rankings and then uses the tug of war formulas to determine who has a higher chance of winning
and then assigns a point based on the point system we designed earlier in the code....WIN = 3 , DRAW = 1, LOSS = 0...
'''

def simulate_match(team_a, team_b):
    # Fetching raw stats from the team_stats dictionary
        stats_a = team_stats[team_a]
        stats_b = team_stats[team_b]
        
        # Getting the multipliers based on the FIFA rankings
        mult_a = get_multiplier(team_a)
        mult_b = get_multiplier(team_b)
        
        # Applying to the historical multipliers
        adj_win_a, adj_loss_a, adj_tie_a = stats_a[0] * mult_a, stats_a[1] * mult_a, stats_a[2] * mult_a
        adj_win_b, adj_loss_b, adj_tie_b = stats_b[0] * mult_b, stats_b[1] * mult_b, stats_b[2] * mult_b
        
        # the tug-of-war formulas
        weight_win_a = adj_win_a + adj_loss_b
        weight_win_b = adj_win_b + adj_loss_a
        weight_tie = adj_tie_a + adj_tie_b
        
        outcomes = ["WIN_A", "WIN_B", "DRAW"]
        match_weights = [weight_win_a, weight_win_b, weight_tie]
        
        sim_result = random.choices(outcomes, weights=match_weights, k=1)[0]
        
       # PENALTY SHOOTOUT IS CONSIDERED A 50-50 CHANCE
        if sim_result == "DRAW":
            shootout_outcomes = ["WIN_A", "WIN_B"]
            sim_result = random.choice(shootout_outcomes)
            
        #We then return the string name of the winning team
        if sim_result == "WIN_A":
            return team_a
        else:
            return team_b

def simulate_match_knockout(team_a, team_b):
    # Fetching raw stats from the team_stats dictionary
        stats_a = team_stats[team_a]
        stats_b = team_stats[team_b]
        
        # Getting the multipliers based on the FIFA rankings
        mult_a = get_multiplier_knockouts(team_a)
        mult_b = get_multiplier_knockouts(team_b)
        
        # Applying to the historical multipliers
        adj_win_a, adj_loss_a, adj_tie_a = stats_a[0] * mult_a, stats_a[1] * mult_a, stats_a[2] * mult_a
        adj_win_b, adj_loss_b, adj_tie_b = stats_b[0] * mult_b, stats_b[1] * mult_b, stats_b[2] * mult_b
        
        # the tug-of-war formulas
        weight_win_a = adj_win_a + adj_loss_b
        weight_win_b = adj_win_b + adj_loss_a
        weight_tie = adj_tie_a + adj_tie_b
        
        outcomes = ["WIN_A", "WIN_B", "DRAW"]
        match_weights = [weight_win_a, weight_win_b, weight_tie]
        
        sim_result = random.choices(outcomes, weights=match_weights, k=1)[0]
        
       # PENALTY SHOOTOUT IS CONSIDERED A 50-50 CHANCE
        if sim_result == "DRAW":
            shootout_outcomes = ["WIN_A", "WIN_B"]
            sim_result = random.choice(shootout_outcomes)
            
        #We then return the string name of the winning team
        if sim_result == "WIN_A":
            return team_a
        else:
            return team_b

def simulate_match_finals(team_a, team_b):
    # Fetching raw stats from the team_stats dictionary
        stats_a = team_stats[team_a]
        stats_b = team_stats[team_b]
        
       
        
        # Applying to the historical multipliers
        adj_win_a, adj_loss_a, adj_tie_a = stats_a[0], stats_a[1] , stats_a[2] 
        adj_win_b, adj_loss_b, adj_tie_b = stats_b[0], stats_b[1] , stats_b[2]
        
        # the tug-of-war formulas
        weight_win_a = adj_win_a + adj_loss_b
        weight_win_b = adj_win_b + adj_loss_a
        weight_tie = adj_tie_a + adj_tie_b
        
        outcomes = ["WIN_A", "WIN_B", "DRAW"]
        match_weights = [weight_win_a, weight_win_b, weight_tie]
        
        sim_result = random.choices(outcomes, weights=match_weights, k=1)[0]
        
       # PENALTY SHOOTOUT IS CONSIDERED A 50-50 CHANCE
        if sim_result == "DRAW":
            shootout_outcomes = ["WIN_A", "WIN_B"]
            sim_result = random.choice(shootout_outcomes)
            
        #We then return the string name of the winning team
        if sim_result == "WIN_A":
            return team_a
        else:
            return team_b
               
championship_tracker = {team: 0 for group in world_cup_groups.values() for team in group}

total_runs = 100000

for run in range(total_runs):

    # We re-initialize each team's initial score to zero inside the loop for every single independent simulation run
    team_score = {}
    for group_name, team_list in world_cup_groups.items():
        for team in team_list:
            team_score[team] = 0

    # MAIN GROUP STAGE SIMULATION
    for group_name, matches in group_stage_matches.items():
        for match in matches:
            team_a, team_b = match[0], match[1]

            # Unpack variables safely so the dictionary list NEVER mutates
            win_a, loss_a, tie_a, _ = team_stats[team_a]
            win_b, loss_b, tie_b, _ = team_stats[team_b]

            mult_a = get_multiplier(team_a)
            mult_b = get_multiplier(team_b)
            
            # Apply multipliers safely to your local variables
            adj_win_a, adj_loss_a, adj_tie_a = win_a * mult_a, loss_a * mult_a, tie_a * mult_a
            adj_win_b, adj_loss_b, adj_tie_b = win_b * mult_b, loss_b * mult_b, tie_b * mult_b
            
        
            #In here we define the MAIN Tug-of-War Probability Formula which will decide which team will win/loss and tie
            weight_win_a = adj_win_a + adj_loss_b
            weight_win_b = adj_win_b + adj_loss_a
            weight_tie   = adj_tie_a + adj_tie_b
            
            # We then use random function to determine the result based on the weight_win_a , weight_win_b and weight_tie variables
            #The weighted variables can be simply explained as the advantage of team a winning vs b and vice versa or even a tie
            outcomes = ["WIN_A", "WIN_B", "DRAW"]  #Outcomes are defined
            Weight_of_match = [weight_win_a, weight_win_b, weight_tie] #Weight of the match...i.e on what factors will the result depend on
            sim_result = random.choices(outcomes, weights=Weight_of_match, k=1)[0]
            
            #In this part the point system we designed earlier is applied 
            if sim_result == "WIN_A":
                team_score[team_a] += win_point
                team_score[team_b] += loss_point
            elif sim_result == "WIN_B":
                team_score[team_b] += win_point
                team_score[team_a] += loss_point
            else:
                team_score[team_a] += tie_point
                team_score[team_b] += tie_point

    #NOW PRINTING THE FINAL GROUP STAGE SCORE CARD
    '''
    THIS PART WILL BE USED TO PRINT THE GROUP STANDINGS ...BUT WE WILL RUN THIS SIMULATION A LOT OF TIMES 
    SO PRINTING EVERY TIME IS NOT REQUIRED.

    print("FINAL GROUP STANDINGS")

    for group_name, team_list in world_cup_groups.items():
        print(f"\n{group_name}:")
        
        #A table is created for 4 teams in the respective group
        group_data = []
        for team in team_list:
            group_data.append({
                "Team": team, 
                "Points": team_score[team]
            })
        
        # The data is properly turned to a clean Pandas DataFrame
        group_df = pd.DataFrame(group_data)
        
        #The dataframe is then sorted from highest to lowest points 
        sorted_df = group_df.sort_values(by="Points", ascending=False)
        
        #FINAL PRINTING OF GROUP STAGE DATA
        print(sorted_df.to_string(index=False))
    '''


    '''
    #DECIDING WHICH TEAMS PROCEED TO THE ROUND OF 32
    First we decide which teams are going to proceed to the knockouts..
    Here i'm going to use a sample progam which will later me commented
    Basically we are going to create a whole new csv file which will show each team's chances of proceeding to round of 32
    Later we will use similar simution for the whole tournament

    Top 2 teams from each group are automatically qualified.But we will creata a separate table for teams 
    in 3rd place and choose the best 8 out of 12.TO handle tie breakers, i have decided that we will use the goals per match data of a team
    from the World Cup Final Data csv file. 

    ASSUMPTION: I AM CONSIDERING THAT IF A TEAM HAS HIGHER GOAL PER MATCH IT IS AN AGREESIVE TEAM AND HAS A HIGHER CHANCE 
    OF HAVING MORE GOAL DIFFERANCE..GOAL DIFFERANCE DEPENDS ON THE AGRESSIVENESS OF BOTH THE TEAMS SO YES THIS IS NOT PROPERLY ACCURATE
    BUT TO MAKE SURE THE CODE IS SIMPLE...MATHEMATICALLY WE ARE ASSUMING THIS.
    '''

    #Top 2 automatically qualifies to ROUND OF 32
    automatic_qualifiers = []
    third_place_candidates = []

    for group_name, team_list in world_cup_groups.items():
        
        # Gathering the data and rank from group stage
        group_ranks = []
        for team in team_list:
            points = team_score[team]
            g_per_match = team_stats[team][3] # Fetching the goals per match for tie breakers
            group_ranks.append((team, points, g_per_match))
        
        # Sorting first by points, then by goals_per_match if points are same for 2 teams
        # reverse=True is used to make sure that highest values go to the top
        # the sorting technique used will be explained in the readme file
        sorted_group = sorted(group_ranks, key=lambda x: (x[1], x[2]), reverse=True)
        
        #Top 2 teams automatically move on to the Round of 32 list
        automatic_qualifiers.append(sorted_group[0][0]) # 1st Place team on the group
        automatic_qualifiers.append(sorted_group[1][0]) # 2nd Place team on the group
        
        #3rd Place team goes to the wildcard table which will be initialized next and top 8 qualifies
        third_place_candidates.append(sorted_group[2])
    #Using the exact same logic above we rank all the 12 3rd placed teams
    sorted_wildcards = sorted(third_place_candidates, key=lambda x: (x[1], x[2]), reverse=True)
    # We bring out the top 8 wildcard teams
    wildcard_winners = []
    for i in range(8):
        wildcard_winners.append(sorted_wildcards[i][0])
    

    #THE FINAL TEAMS IN ROUND OF 32 IS CREATED
    r_of_32 = automatic_qualifiers + wildcard_winners


    #For checking purposes print may be used...
    #print(r_of_32)

    #NOW WE DEFINE WHICH 16 TEAMS WILL GO TO NEXT STAGE
    random.shuffle(r_of_32)
    
    #ROUND OF 32 -----> ROUND OF 16
    #random.shuffle(r_of_32)
    r_of_16 = []
    for i in range(0, len(r_of_32), 2):
        winner = simulate_match_knockout(r_of_32[i], r_of_32[i+1])
        r_of_16.append(winner)

    #For verification purposes we can print it
    #print(r_of_16)    

    #ROUND OF 16 -----> QUATERFINALS
    #random.shuffle(r_of_16)
    q_finals = []
    for i in range(0, len(r_of_16), 2):
        winner = simulate_match_knockout(r_of_16[i], r_of_16[i+1])
        q_finals.append(winner)

    #For verification purposes we can print it
    #print(q_finals)   

    #QUATERFINALS -----> SEMIFINALS
    #random.shuffle(q_finals)
    s_finals = []
    for i in range(0, len(q_finals), 2):
        winner = simulate_match_knockout(q_finals[i], q_finals[i+1])
        s_finals.append(winner)

    #For verification purposes we can print it
    #print(s_finals)   

    #SEMIFINALS -----> GRAND FINALS
    #random.shuffle(q_finals)
    g_finals = []
    for i in range(0, len(s_finals), 2):
        winner = simulate_match_knockout(s_finals[i], s_finals[i+1])
        g_finals.append(winner)

    #For verification purposes we can print it
    #print(g_finals)   

    champion = simulate_match_finals(g_finals[0],g_finals[1])
    #print('CHAMPION IS', champion)
    # Incrementing the champion's trophy count here
    championship_tracker[champion] += 1

#FINAL SAVING OF ALL THE DATA
results_data = []
for team, trophies in championship_tracker.items():
    win_percentage = (trophies / total_runs) * 100
    results_data.append({
        "team_name": team,
        "trophies_won": trophies,
        "championship_probability (%)": round(win_percentage, 2)
    })

# Convert the structure array into a Pandas DataFrame and organize by sorting frequencies descending
df_predictions = pd.DataFrame(results_data)
df_predictions = df_predictions.sort_values(by="trophies_won", ascending=False)

# Write clean prediction metrics straight into your specified file directory path
output_file_path = r'C:\Users\anath\OneDrive\Desktop\Projects\Probability\Championship_Simulation_Results.csv'
df_predictions.to_csv(output_file_path, index=False)



print("SUCCESFULLY SIMULATED THE WORLD CUP 100000 TIMES")





