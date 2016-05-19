import random
 
with open('uniformevens', 'w') as evens:
        for i in range(0, 2000, 2):
                evens.write("+1 1:" + str(random.uniform(0, 10)) + " 2:" + str(random.uniform(0, 10)) + "\n")

with open('uniformodds', 'w') as odds:
        for i in range(1, 2000, 2):
                odds.write("+1 1:" + str(random.uniform(0, 10)) + " 2:" + str(random.uniform(0, 10)) + "\n")