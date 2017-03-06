import random

size = 200000
table = [[0 for i in range(3)] for i in range(size)] 

for i in range(size):
	f1 = random.uniform(-1, 1)
	f2 = random.uniform(-1, 1)
	if f1 ** 2 + f2 ** 2 <= 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2

with open('TestCircleHardTraining.txt', 'w') as training, open('TestCircleHardTestingAll.txt', 'w') as testingall, open('TestCircleHardTestingSignal.txt', 'w') as testingsignal, open('CircleHardTestingBackground.txt', 'w') as testingbackground:
	for i in range(0, size, 2):
		training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
	for i in range(1, size, 2):
		testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		if table[i][0] == "+1":
			testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		else:
			testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")