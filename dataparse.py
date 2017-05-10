"""
Created on Sat Apr 29 21:55:32 2017

@author: vinaya,mohanakrishna
"""
from __future__ import division
import pandas as pd
import math
 
dataset = pd.read_csv("match_data.csv")


#Calculating Past Performance
dataset['past_perf_home'] = 0.0
dataset['past_perf_away'] = 0.0
k = 10

def calculatePerfLastK(index,team):
    localK = k
    if(index<k):
        #print(dataset.iloc[index][0])
        localK = index
    perfK = 0
    count = 0
    result = 0
    for i in range(index-1,0,-1):
        if(count>=localK):
            break;
        if(dataset.iloc[i]['home_team']==team):
            count+=1
            perfK+=dataset.iloc[i]['home_team_goal']
        elif(dataset.iloc[i]['away_team']==team):
            count+=1
            perfK+=dataset.iloc[i]['away_team_goal']
    if(count!=0):
        result=perfK/count
    return result

for index, row in dataset.iterrows():
     
     dataset.set_value(index,'past_perf_home',calculatePerfLastK(index,row['home_team']))
     dataset.set_value(index,'past_perf_away',calculatePerfLastK(index,row['away_team']))



#Calculate home and away player rating avg
dataset['home_player_avg']=0.0
dataset['a']=0.0
       
for index, row in dataset.iterrows():
    home_total = 0.0
    away_total = 0.0
    
    for i in range(1,11):
        temp = 'home_player_'+str(i)
        home_total+=row[temp]
    dataset.set_value(index,'home_player_avg',(home_total/11.0))
       
    for i in range(1,11):
        temp1 = 'away_player_'+str(i)
        away_total+=row[temp1]
    dataset.set_value(index,'away_player_avg',(away_total/11.0))
    

player = pd.read_csv("player.csv")
match = dataset
temp = None

count =1
for index, row in match.iterrows():
    newPlayer = 0.0
    
    if(math.isnan(row['home_player_1'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_1']]
        newPlayer = temp['rating']   
    match.set_value(index,'home_player_1',newPlayer)
    
    if(math.isnan(row['home_player_2'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_2']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_2',newPlayer)
        
    if(math.isnan(row['home_player_3'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_3']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_3',newPlayer)

    if(math.isnan(row['home_player_4'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_4']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_4',newPlayer)
        
    if(math.isnan(row['home_player_5'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_5']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_5',newPlayer)
        
    if(math.isnan(row['home_player_6'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_6']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_6',newPlayer)

    if(math.isnan(row['home_player_7'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_7']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_7',newPlayer)

    if(math.isnan(row['home_player_8'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_8']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_8',newPlayer)

    if(math.isnan(row['home_player_9'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_9']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_9',newPlayer)

    if(math.isnan(row['home_player_10'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_10']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_10',newPlayer)

    if(math.isnan(row['home_player_11'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['home_player_11']]
        newPlayer = temp['rating']
    match.set_value(index,'home_player_11',newPlayer)
    
    
    if(math.isnan(row['away_player_1'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_1']]
        newPlayer = temp['rating']   
    match.set_value(index,'away_player_1',newPlayer)
    
    if(math.isnan(row['away_player_2'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_2']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_2',newPlayer)
        
    if(math.isnan(row['away_player_3'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_3']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_3',newPlayer)

    if(math.isnan(row['away_player_4'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_4']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_4',newPlayer)
        
    if(math.isnan(row['away_player_5'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_5']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_5',newPlayer)
        
    if(math.isnan(row['away_player_6'])):
        newPlayer = 0.0
    else:
        temp = player.loc[player['player_api_id']==row['away_player_6']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_6',newPlayer)

    if(math.isnan(row['away_player_7'])):
        newPlayer = 0.0
    else:
        #print(row['home_player_1'])
        temp = player.loc[player['player_api_id']==row['away_player_7']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_7',newPlayer)

    if(math.isnan(row['away_player_8'])):
        newPlayer = 0.0
    else:
        #print(row['home_player_1'])
        temp = player.loc[player['player_api_id']==row['away_player_8']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_8',newPlayer)

    if(math.isnan(row['away_player_9'])):
        newPlayer = 0.0
    else:
        #print(row['home_player_1'])
        temp = player.loc[player['player_api_id']==row['away_player_9']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_9',newPlayer)

    if(math.isnan(row['away_player_10'])):
        newPlayer = 0.0
    else:
        #print(row['home_player_1'])
        temp = player.loc[player['player_api_id']==row['away_player_10']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_10',newPlayer)

    if(math.isnan(row['away_player_11'])):
        newPlayer = 0.0
    else:
        #print(row['home_player_1'])
        temp = player.loc[player['player_api_id']==row['away_player_11']]
        newPlayer = temp['rating']
    match.set_value(index,'away_player_11',newPlayer)

dataset.to_csv("updated_match.csv")