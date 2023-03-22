"""
The file ALE2022.txt Download ALE2022.txt contains the number of games won and lost by each MLB team in the AL East in
 2022. Write a Python program that opens and read the contents of the file, computes the winning percentage of each
 team, and prints each team and its winning percentage. (winning percentage = games won / (games won + games lost)
"""

scores = open("ALE2022.txt", mode='r')

teams = students = scores.readlines()

for n in teams:
    parts = n.split()
    winning_percentage = float(parts[1]) / (float(parts[1]) + float(parts[2]))
    winning_percentage = winning_percentage * 100
    print("The team:", parts[0], "has a winning percentage of %{}.".format(round(winning_percentage, 2)))

