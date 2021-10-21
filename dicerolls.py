import random 

two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
eleven = []
twelve = []

throws = 1_000

for i in range(throws):
    dice = [random.randint(1, 6), random.randint(1, 6)]
    
    dicesum = dice[0] + dice[1]
    
    if dicesum == 2:
        two.append(1)
        
    elif dicesum == 3:
        three.append(1)
        
    elif dicesum == 4:
        four.append(1)
        
    elif dicesum == 5:
        five.append(1)

    elif dicesum == 6:
        six.append(1)

    elif dicesum == 7:
        seven.append(1)

    elif dicesum == 8:
        eight.append(1)

    elif dicesum == 9:
        nine.append(1)

    elif dicesum == 10:
        ten.append(1)

    elif dicesum == 11:
        eleven.append(1)

    elif dicesum == 12:
        twelve.append(1)

# print(f"two {len(two)}")
# print(f"three {len(three)}")
# print(f"four {len(four)}")
# print(f"five {len(five)}")
# print(f"six {len(six)}")
# print(f"seven {len(seven)}")
# print(f"eight {len(eight)}")
# print(f"nine {len(nine)}")
# print(f"ten {len(ten)}")
# print(f"eleven {len(eleven)}")
# print(f"twelve {len(twelve)}")

two = 27835
three = 55555
four = 83202
five = 111432
six = 138158
seven = 167197
eight = 138625
nine = 111391
ten = 83017
eleven = 55831
twelve = 27757

list = [two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
precentages = [2.7835, 5.5555, 8.3202, 11.1432, 13.8158, 16.7197, 13.8625, 11.1391, 8.3017, 5.5831, 2.7757]


# for element in list:
#     percent = element * 100 / 1_000_000
#     precentages.append(percent)

# print(sum([2.7835, 5.5555, 8.3202, 11.1432, 13.8158, 16.7197, 13.8625, 11.1391, 8.3017, 5.5831, 2.7757]))

# 1_000_000
# two 27522
# three 55472
# four 83568
# five 110721
# six 138819
# seven 166475
# eight 139686
# nine 110756
# ten 83711
# eleven 55456
# twelve 27814