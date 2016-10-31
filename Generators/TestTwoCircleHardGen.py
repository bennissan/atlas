import random

size = 200000
table = [[0 for i in range(3)] for i in range(size)] 

for i in range(size):
	f1 = random.uniform(-1.5, 1.5)
	f2 = random.uniform(-1.5, 1.5)
	if (f1 - 0.5) ** 2 + (f2 - 0.5) ** 2 <= 1 or (f1 + 0.5) ** 2 + (f2 + 0.5) ** 2 <= 1:
		table[i][0] = "+1"
	else:
		table[i][0] = "-1"
	table[i][1] = f1
	table[i][2] = f2

with open('TestTwoCircleHardTraining', 'w') as training, open('TestTwoCircleHardTestingAll', 'w') as testingall, open('TestTwoCircleHardTestingSignal', 'w') as testingsignal, open('TestTwoCircleHardTestingBackground', 'w') as testingbackground:
	for i in range(0, size, 2):
		training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
	for i in range(1, size, 2):
		testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		if table[i][0] == "+1":
			testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")
		else:
			testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + "\n")