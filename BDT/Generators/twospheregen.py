import random

table = [[0 for x in range(4)] for x in range(10000)] 

for i in range(10000):
	table [i][1] = random.uniform(0, 10)
	table[i][2] = random.uniform(0, 10)
	table [i][3] = random.uniform(0, 10)

	x = table[i][1]; y = table[i][2]; z = table[i][3]

	if (x - 2) ** 2 + (y - 2) ** 2 + (z - 2) ** 2 <= 4 or (x - 6) ** 2 + (y - 6) ** 2  + (z - 6) ** 2 <= 2:
		Class = 1
	else:
		Class = -1
	if 2.25 < (x - 2) ** 2 + (y - 2) ** 2 + (z - 2) ** 2 < 6.25 or 2.25 < (x - 6) ** 2 + (y - 6) ** 2 + (z - 6) ** 2 < 6.25:
		if random.random() <= .1:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"

with open('twosphereevens', 'w') as evens:
	for i in range(0, 10000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		Feature3 = str(table[i][3])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2 + " 3:" + Feature3
		evens.write(line + "\n")

with open('twosphereodds', 'w') as odds:
	for i in range(1, 10000, 2):
		Class = table[i][0]
		Feature1 = str(table[i][1])
		Feature2 = str(table[i][2])
		Feature3 = str(table[i][3])
		line = Class + " 1:" + Feature1 + " 2:" + Feature2 + " 3:" + Feature3
		odds.write(line + "\n")