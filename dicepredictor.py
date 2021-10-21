import random

class Agent:
    def __init__(self, smart):
        #0 is random and 1 is smart
        self.smart = smart
        
    # Since both the smart and NotSmart agent are sharing the same class the function is to decide which decision making function they will 
    # use based on whether the are a smart agent or NotSmart agent as will be specified when instatiating the objects below (i.e mike and harry)
    def decision(self):
        if self.smart == 0:
            return self.randpredict()
        elif self.smart == 1:
            return self.smartpredict()
        
    # function for predicting random values. This is the function that the random guesser agent will use AKA the NotSmart Agent
    def randpredict(self):
        predictions = [ [random.randint(2, 6), random.randint(2, 6)], [random.randint(2, 6), random.randint(2, 6)], [random.randint(2, 6), random.randint(2, 6)], [random.randint(2, 6), random.randint(2, 6)], [random.randint(2, 6), random.randint(2, 6)], [random.randint(2, 6), random.randint(2, 6)] ]
        return predictions
    
    # function for predicting values with the highest chance of occuring based on my dice probability program. This is the function that smart agent will use
    def smartpredict(self):
        predictions = [ [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [1, 6] ]
        # [16,61,25,52,34,43]
        return predictions

    
mike = Agent(0) #random agent
harry = Agent(1) #smart agent

mike_points_sum = []
harry_points_sum = []

mike_points_doubles = []
harry_points_doubles = []

mike_wins = []
harry_wins = []

mike_lose = []
harry_lose = []

evens = []
odds = []

for tries in range(10):
        # rolling the dice
        dice = [random.randint(1, 6), random.randint(1, 6)]
        
        # getting the sum of the faces of the dice thrown
        dicesum = dice[0] + dice[1]
        
        if dicesum % 2 == 0 or dicesum == 7:
            evens.append(dicesum)
        else:
            odds.append(dicesum)
        
        for chance in odds:
            if chance == 7:
                odds.remove(chance)
        # printing the dice faces and the dicesum
        # print(f"dicesum {dicesum}")
        # print(f"dice {dice}")
        
        #mike and harry make a prediction (Note: Even if im throwing the dice before mike and harry's prediction it doesnt really matter becasue these agents cant see the dice)
        mike_prediction = mike.decision()
        harry_prediction = harry.decision()
        
        
        for predict in mike_prediction:
            # summing agent roll
            predictsum = predict[0] + predict[1]
            
            # # scoring for double or an equal sum to the dicesum thrown
            # if predict == dice or predictsum == dicesum:
            #     mike_points.append(1)
            # else:
            #     mike_points.append(0)
            
            #scoring for an equal sum to the dicesum thrown
            if predictsum == dicesum:
                mike_points_sum.append(1)
                mike_wins.append(1)
            else:
                mike_points_sum.append(0)
                mike_lose.append(0)
                
            # scoring for double
            if predict == dice:
                mike_points_doubles.append(1)
                mike_wins.append(1)
            else:
                mike_points_doubles.append(0)
                mike_lose.append(0)
                
        for predict in harry_prediction:
            
            # summing agent roll
            predictsum = predict[0] + predict[1]
            
            # # scoring for double or an equal sum to the dicesum thrown
            # if predict == dice or predictsum == dicesum:
            #     harry_points.append(1)
            # else:
            #     harry_points.append(0)
        
            #scoring for an equal sum to the dicesum thrown
            if predictsum == dicesum:
                # print(f"harrysum {predictsum}")
                
                harry_points_sum.append(1)
                harry_wins.append(1)
            else:
                harry_points_sum.append(0)
                harry_lose.append(0)
                
            # scoring for double
            if predict == dice:
                # print(f"harry {predict}")
                harry_points_doubles.append(1)
                harry_wins.append(1)
            else:
                harry_points_doubles.append(0)
                harry_lose.append(0)

print(evens)
print(odds)

# print(mike_points_sum)
# print(harry_points_sum)
    
# print(mike_points_doubles)
# print(harry_points_doubles)

print(mike_wins)
# print(mike_lose)

print(harry_wins)
# print(harry_lose)

# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] harry

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] harry

# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1]

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] mike
# [1, 1, 1, 1, 1, 1, 1, 1, 1]