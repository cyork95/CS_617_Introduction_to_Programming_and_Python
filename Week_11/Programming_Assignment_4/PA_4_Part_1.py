"""
The file Cities.txt contains information about the 25 largest cities in the United States.
Each line of the file has four fields — name, state, population in 2000 (in 100,000s), and population in
2010 (in 100,000s). Write a program that reads the data from this file and outputs the name of a city and its
percentage population growth from 2000 to 2010. The cities should be output in decreasing order by their percent
population growth.
"""

file = open("Cities.txt", mode='r')
cities = file.readlines()
city_dict = {}

for city in cities:
    city = city.strip()
    city_parts = city.split(",")
    city_name = city_parts[0]
    pop_in_2000 = city_parts[2]
    pop_in_2010 = city_parts[3]
    population_growth = float(pop_in_2010) / float(pop_in_2000)
    population_growth = round((population_growth * 100),2)
    city_dict[population_growth] = city_name

city_dict = sorted(city_dict.items(), reverse=True)

for item in city_dict:
    print(f'City: {item[1]} *** Population Growth: {item[0]}')


