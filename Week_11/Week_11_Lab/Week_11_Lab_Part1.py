"""
The file WorldSeriesWinners.txt contains a chronological list of the World Series’ winning teams from 1903 through 2009.
 The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that
 won in 2009. (Note the World Series was not played in 1904 or 1994. There are entries in the file indicating this.)
 Write a program that reads this file and creates a dictionary in which the keys are the names of the teams, and each
 key’s associated value is the number of times the team has won the World Series. The program should prompt the user for
  a team name. It should then display the number of times that team has won the World Series.
"""

file = open("WorldSeriesWinners.txt")
winning_teams = file.readlines()
winnings_dict = {}

for winner in winning_teams:
    winner = winner.strip()
    winning_team = winner.split("\n")
    if winning_team[0] in winnings_dict:
        winnings_dict[winning_team[0]] += 1
    elif "World Series Not Played" in winning_team[0]:
        continue
    else:
        winnings_dict[winning_team[0]] = 1

winnings_dict = sorted(winnings_dict.items())


def find_team(team):
    for key, value in winnings_dict:
        if team in key.lower():
            team_string = f"Your team {key} has won {value} times!"
            return team_string
        else:
            continue


team = input("Enter a team name to check if that team won a World Series: ")
team.lower()

team_string = find_team(team)

if team_string is None:
    print("Sorry I couldn't find your team! Try again?")
else:
    print(team_string)