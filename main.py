import random
import csv


class Property:
    def __init__(self, name, position, price, rent, visited=0, value=0, isproperty=True):
        self.name = name
        self.position = position
        self.price = price
        self.rent = rent
        self.visited = visited
        self.value = value
        self.isproperty = isproperty


Go = Property("Go", 0, 100, 1)
Old_kent = Property("Old_kent", 1, 600, 20)
First_community_chest = Property("First_community_chest", 2, 100, 1)
White_chapel = Property("White_chapel", 3, 600, 40)
Income_Tax = Property("Income_Tax", 4, 0, 2000)
King_cross_station = Property("King_cross_station", 5, 2000, 250)
The_angel_islington = Property("The_angel_islington", 6, 1000, 60)
First_chance = Property("First_chance", 7, 100, 1)
Euston = Property("Euston", 8, 1000, 60)
Pentoville = Property("Pentoville", 9, 1200, 80)
Just_visiting = Property("Just_visiting", 10, 100, 1)
Pall_mall = Property("Pall_mall", 11, 1400, 100)
Electric_company = Property("Electric_company", 12, 1500, 80)
White_hall = Property("White_hall", 13, 1400, 100)
Northhumber = Property("Northhumber", 14, 1600, 120)
Maryleborne_station = Property("Maryleborne_station", 15, 2000, 250)
Bow_street = Property("Bow_street", 16, 1800, 140)
Second_community_chest = Property("Second_community_chest", 17, 100, 1)
Marlborough_street = Property("Marlborough_street", 18, 1800, 140)
Vine_street = Property("Vine_street", 19, 2000, 160)
Free_parking = Property("Free_parking", 20, 100, 1)
Strand = Property("Strand", 21, 2200, 180)
Second_chance = Property("Second_chance", 22, 100, 1)
Fleet_street = Property("Fleet_street", 23, 2200, 180)
Transfalgar_square = Property("Transfalgar_square", 24, 2400, 200)
Fenchchurch_station = Property("Fenchchurch_station", 25, 2000, 250)
leicester_square = Property("leicester_square", 26, 2600, 220)
Conventry_street = Property("Conventry_street", 27, 2600, 220)
Water_works = Property("Water_works", 28, 1500, 80)
Picadilly = Property("Picadilly", 29, 2800, 240)
Go_to_jail = Property("Go_to_jail", 30, 100, 1)
Regent_street = Property("Regent_street", 31, 3000, 260)
Oxford_street = Property("Oxford_street", 32, 3000, 260)
Third_community_chest = Property("Third_community_chest", 33, 100, 1)
Bond_street = Property("Bond_street", 34, 3200, 280)
Liverpool_station = Property("Liverpool_station", 35, 2000, 250)
Third_chance = Property("Third_chance", 36, 100, 1)
Parklane = Property("Parklane", 37, 3500, 350)
Supertax = Property("Supertax", 38, 0, 1000)
Mayfair = Property("Mayfair", 39, 4000, 500)

properties = [Go, Old_kent, First_community_chest, White_chapel, Income_Tax, King_cross_station, The_angel_islington,
              First_chance, Euston, Pentoville, Just_visiting, Pall_mall, Electric_company, White_hall, Northhumber,
              Maryleborne_station, Bow_street, Second_community_chest, Marlborough_street, Vine_street, Free_parking,
              Strand, Second_chance, Fleet_street, Transfalgar_square, Fenchchurch_station, leicester_square,
              Conventry_street, Water_works, Picadilly, Go_to_jail, Regent_street, Oxford_street, Third_community_chest,
              Bond_street, Liverpool_station, Third_chance, Parklane, Supertax, Mayfair]

i = 0
initial_position = random.randint(2, 12)
header = ['Property Name', 'Visits', 'Values Accumulated',
          'Trial Number', 'Position Number']
rows = []
rolls = 100_000

# for player in range(6):
while i <= rolls:
    for property in properties:
        if property.position == initial_position:
            if property.name == "Go_to_jail":
                state = []
                property.visited += 1
                property.value += property.rent

                state.append(property.name)
                state.append(property.visited)
                state.append(property.value)
                state.append(i)
                state.append(initial_position)
                rows.append(state)

                initial_position = 10

                # print("went to jail")
                # print(f"Property name {property.name}")
                # print(f"Number of visits {property.visited}")
                # print("\n")
            else:
                property.visited += 1
                property.value += property.rent

                state = []
                state.append(property.name)
                state.append(property.visited)
                state.append(property.value)
                state.append(i)
                state.append(initial_position)
                rows.append(state)

                # print(initial_position)
                # print(f"Property name {property.name}")
                # print(f"Number of visits {property.visited}")
                # print(f"Value accumulated {property.value}")
                # print("\n")

    next_position = random.randint(2, 12) + initial_position

    if next_position > 39:
        pos_value = next_position - 39
        initial_position = pos_value - 1
    else:
        initial_position = next_position

    i += 1


# print(rows)
# print(max(rows, key=lambda x: x[2]))

new_rows = []

for property in properties:
    analyzed_rows = []
    for row in rows:
        if property.name == row[0]:
            # print(row)
            property_outcomes = []
            property_outcomes.append(row[0])  # name
            property_outcomes.append(row[1])  # visited
            property_outcomes.append(row[2])  # value
            property_outcomes.append(row[3])  # at dice roll number n
            property_outcomes.append(row[4])  # position in board
            analyzed_rows.append(property_outcomes)

    # print(analyzed_rows)
    new_rows.append(analyzed_rows)


# print(new_rows)
analyzed_data = []

for row in new_rows:
    property_data = max(row, key=lambda x: x[2])
    analyzed_data.append(property_data)

# print(analyzed_data)

filename = "monopoly_" + str(rolls) + "_rolls_data.csv"

raw_data = "monopoly_" + str(rolls) + "_rolls_raw_data.csv"

# go to jail is in 30
# go to jail is in 10

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(analyzed_data)

with open(raw_data, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
