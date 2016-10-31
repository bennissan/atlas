import random

size = 200000
table = [[0 for i in range(4)] for i in range(size)] 

for i in range(size):
	f1 = random.uniform(0, 10)
	f2 = random.uniform(0, 10)
	f3 = random.uniform(0, 10)
	if (f1 - 2) ** 2 + (f2 - 2) ** 2 + (f3 - 2) ** 2 <= 4 or (f1 - 7) ** 2 + (f2 - 7) ** 2  + (f3 - 7) ** 2 <= 4:
		Class = 1
	else:
		Class = -1
	if 2.75 < (f1 - 2) ** 2 + (f2 - 2) ** 2 + (f3 - 2) ** 2 < 5.25 or 2.75 < (f1 - 7) ** 2 + (f2 - 7) ** 2 + (f3 - 7) ** 2 < 5.25:
		if random.random() <= .15:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2
	table[i][3] = f3

with open('TwoSphereSoftTraining', 'w') as training, open('TwoSphereSoftTestingAll', 'w') as testingall, open('TwoSphereSoftTestingSignal', 'w') as testingsignal, open('TwoSphereSoftTestingBackground', 'w') as testingbackground:
	for i in range(0, size, 2):
		training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")
	for i in range(1, size, 2):
		testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")
		if table[i][0] == "+1":
			testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")
		else:
			testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + "\n")