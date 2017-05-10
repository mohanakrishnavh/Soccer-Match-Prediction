# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:31:00 2017

@author: Mohanakrishna
"""

from __future__ import division
import pandas as pd


dataset = pd.read_csv("updated_match.csv")


dir = "..\\datasets"
txtDir = "txt"
teamName = ""
teams = []
teamSignificance = ""
opponentTeamSignificance = ""
teamsStat = []

def getTeamsNamesList():
    team_list = set(dataset.home_team)
    list2 = (set(dataset.away_team))
    team_list |= list2
    teams.extend(team_list)

def getInfo(teams, matchesNumber):
    for team in teams:
        parseCSV(team)
        saveResults(teamsStat, team)
        del teamsStat[:]

def parseCSV(teamName):
    
    for index, row in dataset.iterrows():
        try:
            isTeamHome = row['home_team'] == teamName
            isTeamAway = row['away_team']== teamName

            if isTeamHome:
                teamsStat.append([row['home_team'],  row['away_team'],row['home_player_avg'], row['away_player_avg'],row['past_perf_home'], row['past_perf_away'],row['home_team_goal'],row['away_team_goal'],20])
              
            if isTeamAway:
                teamsStat.append([row['away_team'],row['home_team'], row['away_player_avg'],row['home_player_avg'], row['past_perf_away'],row['past_perf_home'],row['away_team_goal'],row['home_team_goal'],10])
        
        except:
            pass

def saveResults(teamsStat, teamName):
    resFile = open(txtDir + "/sortedData" + teamName+ ".txt", 'w')
    for stat in teamsStat:
        resFile.write( ("; ".join( repr(e) for e in stat ))+"\n" )
#        resFile.write(''.join(str(stat)) + '\n')
    resFile.close()

if __name__ == '__main__':
    getTeamsNamesList()
    getInfo(teams, len(teams))    
    
    
    