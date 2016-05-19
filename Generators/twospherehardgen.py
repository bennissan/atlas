import random

table = [[0 for i in range(4)] for i in range(20000)] 

for i in range(20000):
	f1 = random.uniform(0, 10)
	f2 = random.uniform(0, 10)
	f3 = random.uniform(0, 10)
	if (f1 - 2) ** 2 + (f2 - 2) ** 2 + (f3 - 2) ** 2 <= 4 or (f1 - 6) ** 2 + (f2 - 6) ** 2  + (f3 - 6) ** 2 <= 2:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2
	table[i][3] = f3

with open('twospherehardevens', 'w') as evens:
	for i in range(0, 20000, 2):
		evens.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")

with open('twospherehardodds', 'w') as odds:
	for i in range(1, 20000, 2):
		odds.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")