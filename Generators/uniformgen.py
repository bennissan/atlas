import random
 
with open('uniformevens', 'w') as evens:
        for i in range(10000):
                evens.write("+1 1:" + str(random.uniform(0, 10)) + " 2:" + str(random.uniform(0, 10)) + "\n")

with open('uniformodds', 'w') as odds:
        for i in range(10000):
                odds.write("+1 1:" + str(random.uniform(0, 10)) + " 2:" + str(random.uniform(0, 10)) + "\n")