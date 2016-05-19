import random

table = [[0 for i in range(3)] for i in range(20000)] 

for i in range(20000):
	f1 = random.uniform(0, 10)
	f2 = random.uniform(0, 10)
	if (f1 - 2) ** 2 + (f2 - 2) ** 2 <= 4 or (f1 - 6) ** 2 + (f2 - 6) ** 2 <= 2:
		Class = 1
	else:
		Class = -1
	if 2.25 < (f1 - 2) ** 2 + (f2 - 2) ** 2 < 5.75 or 1.5 < (f1 - 6) ** 2 + (f2 - 6) ** 2 < 2.5:
		if random.random() <= .15:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2

with open('twocirclesoftevens', 'w') as evens:
	for i in range(0, 20000, 2):
		evens.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")

with open('twocirclesoftodds', 'w') as odds:
	for i in range(1, 20000, 2):
		odds.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")