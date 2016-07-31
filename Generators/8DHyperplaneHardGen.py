import random

size = 200000
table = [[0 for i in range(9)] for i in range(size)] 

for i in range(size):
        f1 = random.uniform(0, 10); f2 = random.uniform(0, 10)
        f3 = random.uniform(0, 10); f4 = random.uniform(0, 10)
        f5 = random.uniform(0, 10); f6 = random.uniform(0, 10)
        f7 = random.uniform(0, 10); f8 = random.uniform(0, 10)
        if f1 + f2 + f3 + f4 + f5 + f6 + f7 <= f8:
                table[i][0] = "+1"
        else:
                table[i][0] = "-1"
        table[i][1] = f1; table[i][2] = f2
        table[i][3] = f3; table[i][4] = f4
        table[i][5] = f5; table[i][6] = f6
        table[i][7] = f7; table[i][8] = f8
                
with open('8DHyperplaneHardTraining', 'w') as training, open('8DHyperplaneHardTestingAll', 'w') as testingall, open('8DHyperplaneHardTestingSignal', 'w') as testingsignal, open('8DHyperplaneHardTestingBackground', 'w') as testingbackground:
        for i in range(0, size, 2):
                training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
        for i in range(1, size, 2):
                testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
                if table[i][0] == "+1":
                        testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
                else:
                        testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")