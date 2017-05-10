# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:51:01 2017

@author: Mohanakrishna
"""

import os
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

start_path = "txt"
	

def getFilesData(start_path):
	
	listTeamsData = []
	teams_file_names = os.listdir(start_path)

	for i in range(0, len(teams_file_names), 1):
		listTeamsData.append(open(start_path + "/" + teams_file_names[i], 'r'))
	return listTeamsData



def getBatch(listParams, start, finish, X_batch, Y_batch):
    for i in range (start, finish, 1):
        game_x = []
        game_y = -1
        params= (listParams[i].split("\n"))[0].split(";")
        
        game_x=[float(params[2]),float(params[3]),float(params[4]),float(params[5]),int(params[8])]
        goals_1 = params[6]
        goals_2 = params[7]
        if goals_1 > goals_2:
            game_y = 2
        elif goals_1 < goals_2:
            game_y = 0
        else:
            game_y = 1
        X_batch.append(game_x)
        Y_batch.append(game_y)
        
def naiveBayes(train_X, train_Y, test_X):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	model_NB = MultinomialNB()
	model_NB.fit(X, Y)
	predictedNB = model_NB.predict(X_test)
	return predictedNB

def svmachine(train_X, train_Y, test_X):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	clf = svm.SVC(gamma=0.1)
	clf.fit(X, Y)
	predictedSVM = clf.predict(X_test)
	return predictedSVM		

def Nusvmachine(train_X, train_Y, test_X):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	clf = svm.NuSVC(kernel='rbf')
	clf.fit(X, Y)
	predictedSVM = clf.predict(X_test)
	return predictedSVM	


def logisticRegression(train_X, train_Y, test_X):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	model_LR = LogisticRegression()
	model_LR.fit(X, Y)
	predictedLR = model_LR.predict(X_test)
	return predictedLR
  


def nearestNeighbour(train_X, train_Y, test_X):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	neigh = KNeighborsClassifier(n_neighbors=30)
	neigh.fit(X, Y)
	predictedKNN = neigh.predict(X_test)
	return predictedKNN
 

def randomForest(train_X, train_Y, test_X, treeCount):
	X = train_X[:]
	Y = train_Y[:]
	X_test = test_X[:]
	forest = RandomForestClassifier(treeCount)
	forest.fit(X, Y)
	predictedRF = forest.predict(X_test)
	return predictedRF

def methodResults(predictedY, correctY):
	rightCount = 0
	for i in range (0, len(correctY), 1):
		if predictedY[i] == correctY[i]:
			rightCount = rightCount + 1

	percent = (float(rightCount) / len(correctY)) * 100
	print("  Percent: ", percent)

     
X_list = []
Y_list = []
test_batch_X = []
test_batch_Y = []
allGamesCount = 0


teams_files = getFilesData(start_path)


for team_file in teams_files:
	team_games = team_file.readlines()
	#prepare train_batch
	getBatch(team_games, 0, len(team_games) - 4, X_list, Y_list)
	#prepare test_batch
	getBatch(team_games, len(team_games) - 4, len(team_games), test_batch_X, test_batch_Y)
	#allGamesCount = allGamesCount + len(team_games)
    
#creating np data
X_train_np = np.array(X_list)
Y_train_np = np.array(Y_list)
X_test_np = np.array(test_batch_X)
Y_test_np = np.array(test_batch_Y)

predSVM = svmachine(X_train_np, Y_train_np, X_test_np)
print("Results of Support Vectors Machine:")
methodResults(predSVM, Y_test_np)

#predNuSVM = Nusvmachine(X_train_np, Y_train_np, X_test_np)
#print("Results of NuSupport Vectors Machine:")
#methodResults(predNuSVM, Y_test_np)

predNB = naiveBayes(X_train_np, Y_train_np, X_test_np)
print("Results of Naive Bayes:")
methodResults(predNB, Y_test_np)

predLR = logisticRegression(X_train_np, Y_train_np, X_test_np)
print("Results of Logistic Regression:")
methodResults(predLR, Y_test_np)


predKNN = nearestNeighbour(X_train_np, Y_train_np, X_test_np)
print("Results of Nearest Neighbour:")
methodResults(predKNN, Y_test_np)

treesCount = 20
predRF = randomForest(X_train_np, Y_train_np, X_test_np, treesCount)
print("Results of Random Forest:")
methodResults(predRF, Y_test_np)





