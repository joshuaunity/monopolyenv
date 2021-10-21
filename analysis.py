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

Electric_company = Property("Electric_company", 2, 1500, 80)
White_hall = Property("White_hall", 3, 1400, 100)
Northhumber = Property("Northhumber", 4, 1600, 120)
Maryleborne_station = Property("Maryleborne_station", 5, 2000, 250)
Bow_street = Property("Bow_street", 6, 1800, 140)
Second_community_chest = Property("Second_community_chest", 7, 100, 1)
Marlborough_street = Property("Marlborough_street", 8, 1800, 140)
Vine_street = Property("Vine_street", 9, 2000, 160)
Free_parking = Property("Free_parking", 10, 100, 1)
Strand = Property("Strand", 11, 2200, 180)
Second_chance = Property("Second_chance", 12, 100, 1)

properties = [Electric_company, White_hall, Northhumber,Maryleborne_station, Bow_street, Second_community_chest, Marlborough_street, Vine_street, Free_parking,
              Strand, Second_chance]

dice = random.randint(2, 12)

rolls = 1000 #trials
i= 0
rows = []

while i <= rolls:
    for property in properties:
        if dice == property.position:
            state = []
            property.visited += 1
            property.value += property.rent

            state.append(property.name)
            state.append(property.visited)
            state.append(property.value)
            state.append(dice)
            rows.append(state)

            dice = random.randint(2, 12)
        else:
            dice = random.randint(2, 12)
    i += 1

# print(rows)


new_rows = []

for property in properties:
    analyzed_rows = []
    for row in rows:
        if row[0] == property.name:
            # print(row)
            property_outcomes = []
            property_outcomes.append(row[0]) #name
            property_outcomes.append(row[1]) #visited
            property_outcomes.append(row[2]) #value
            property_outcomes.append(row[3]) #at dice roll number n
            analyzed_rows.append(property_outcomes)

    # print(analyzed_rows)    
    new_rows.append(analyzed_rows)  


# print(new_rows)
analyzed_data = []

for row in new_rows:
    property_data = max(row, key=lambda x: x[2])
    analyzed_data.append(property_data)

# print(analyzed_data)

raw_data = "monopoly_" + str(rolls) + "_rolls_from_jail.csv"
header = ['Property Name', 'Visits', 'Values Accumulated', 'Dice outcome']


with open(raw_data, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(analyzed_data)

print(max(analyzed_data, key=lambda x: x[1]))
