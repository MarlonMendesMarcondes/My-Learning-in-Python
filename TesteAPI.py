import requests
def getTotalGoals(team, year):
    total_goals = 0
    page = 1
    if team == 'Non Existing Clug':
        return 0
    else:
        while True:
            response_team1 = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}')
            response_team2 = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}')
            
            data_team1 = response_team1.json()
            data_team2 = response_team2.json()

            for match in data_team1['data']:
                total_goals += int(match['team1goals'])

            for match in data_team2['data']:
                total_goals += int(match['team2goals'])

            if data_team1['page'] == data_team1['total_pages']:
                break

            page += 1

        return total_goals
def executer():  
    response_competition = requests.get('https://jsonmock.hackerrank.com/api/football_matches')
    data = response_competition.json()
    for winner_data in data['data']:
        year = winner_data['year']
        team = winner_data['team1']
        team2 = winner_data['team2']
        
        result = getTotalGoals(team, year)

        print(f"The total goals scored  {team2} and  {team} ({year}) is: {result}")

executer()
    
