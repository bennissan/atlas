import random

size = 200000
table = [[0 for i in range(3)] for i in range(size)] 

for i in range(size):
	f1 = random.uniform(-1.5, 1.5)
	f2 = random.uniform(-1.5, 1.5)
	if (f1 - 0.5) ** 2 + (f2 - 0.5) ** 2 <= 1 or (f1 + 0.5) ** 2 + (f2 + 0.5) ** 2 <= 1:
		Class = 1
	else:
		Class = -1
	if 0.75 < (f1 - 0.5) ** 2 + (f2 - 0.5) ** 2 < 1.25 or 0.75 < (f1 + 0.5) ** 2 + (f2 + 0.5) ** 2 < 1.25:
		if random.random() <= .15:
			Class *= -1
	if Class == 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2

with open('TestTwoCircleSoftTraining.txt', 'w') as training, open('TestTwoCircleSoftTestingAll.txt', 'w') as testingall, open('TestTwoCircleSoftTestingSignal.txt', 'w') as testingsignal, open('TestTwoCircleSoftTestingBackground.txt', 'w') as testingbackground:
	for i in range(0, size, 2):
		training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
	for i in range(1, size, 2):
		testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		if table[i][0] == "+1":
			testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		else:
			testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")