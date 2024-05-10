#!/bin/python3
import requests
import time

#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
start_time = time.time()
def getWinnerTotalGoals(competition, year):
    total_goals = 0
    page = 1
         
    response_competition = requests.get(f'https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}')
    data_competition = response_competition.json()
    winner = data_competition['data'][0]['winner']
    while True:
        response_matches = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&winner={winner}&page={page}')
        data_matches = response_matches.json()
            
        for match in data_matches['data']:
            if match['team1'] == winner:
                total_goals += int(match['team1goals'])
            elif match['team2'] == winner:
                total_goals += int(match['team2goals'])
            
        if data_matches['page'] == data_matches['total_pages']:
            
            break
        print(page)    
        page +=1
        
    return total_goals

def executer():  
    response_competition = requests.get('https://jsonmock.hackerrank.com/api/football_competitions')
    data = response_competition.json()
    for winner_data in data['data']:
        
        competition = winner_data['name']
        print(competition)
        year = winner_data['year']
        print (year)
        winner = winner_data['winner']
        
        result = getWinnerTotalGoals(competition, year)

        print("--- %s seconds ---" % (time.time() - start_time))
        print(f"The total goals scored by {winner} in {competition} ({year}) is: {result}")

executer()

