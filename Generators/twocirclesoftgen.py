import random

table = [[0 for x in range(3)] for x in range(2000)] 

for i in range(2000):
	table [i][1] = random.uniform(0, 10)
	table[i][2] = random.uniform(0, 10)
	x = table[i][1]; y = table[i][2]
	if (x - 2) ** 2 + (y - 2) ** 2 <= 4 or (x - 6) ** 2 + (y - 6) ** 2 <= 2:
		Class = 1
	else:
		Class = -1
	if 2.25 < (x - 2) ** 2 + (y - 2) ** 2 < 5.75 or 1.5 < (x - 6) ** 2 + (y - 6) ** 2 < 2.5:
		if random.random() <= .15:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"

with open('twocirclesoftevens', 'w') as evens:
	for i in range(0, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		evens.write(line + "\n")

with open('twocirclesoftodds', 'w') as odds:
	for i in range(1, 2000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2
		odds.write(line + "\n")