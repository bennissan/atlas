import random

table = [[0 for x in range(3)] for x in range(2000)] 

for i in range(2000):
	x = 2; y = 0
	while (x - 2) ** 2 + (y - 2) ** 2 == 4:
		x = random.uniform(0, 10)
		y = random.uniform(0, 10)
	table[i][1] = x; table[i][2] = y
	if (x - 2) ** 2 + (y - 2) ** 2 <= 4:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"

with open('circlehardevens', 'w') as evens:
	for i in range(0, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		evens.write(line + "\n")

with open('circlehardodds', 'w') as odds:
	for i in range(1, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		odds.write(line + "\n")