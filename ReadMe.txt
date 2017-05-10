Required libraries:
pandas, numpy, sklearn

dataparse.py:
**only run this for the very first time***
input: match_data.csv
	computes the column past_perf_home, past_perf_away for every row
	K is assumed to be 10

	the average player rating for every match is added for home and away team as home_player_avg and away_player_avg

output: updated_match.csv

player_avg_rating.py:
	takes every team matches and writes to separate files under "txt" folder

predict.py:
	analyses data in the files udner txt folder and outputs accuracy by running
	SVM, LogisticRegression, Naive Bayes, K-NN, Random Forest algorithms