import random

table = [[0 for x in range(3)] for x in range(2000)] 

for i in range(2000):
	table[i][1] = random.uniform(0, 10)
	table[i][2] = random.uniform(0, 10)
	x = table[i][1]; y = table[i][2]
	if x <= y:
		Class = 1
	else:
		Class = -1
	if x - 1 < y < x + 1:
		if random.random() <= .1:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"

with open('linearevens', 'w') as evens:
	for i in range(0, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		evens.write(line + "\n")

with open('linearodds', 'w') as odds:
	for i in range(1, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		odds.write(line + "\n")