import random

size = 200000
table = [[0 for i in range(9)] for i in range(size)]

# Generates signal data in first hypersphere by randomly generating points
# in 4-radius hypercube and selecting points that fall within 2-radius
# hypersphere until 10% of total data is generated.
for i in range(int(0.1 * size)):
        while True:
                f1 = random.uniform(-1.5, 1.5); f2 = random.uniform(-1.5, 1.5)
                f3 = random.uniform(-1.5, 1.5); f4 = random.uniform(-1.5, 1.5)
                f5 = random.uniform(-1.5, 1.5); f6 = random.uniform(-1.5, 1.5)
                f7 = random.uniform(-1.5, 1.5); f8 = random.uniform(-1.5, 1.5)
                if (f1 - 0.5) ** 2 + (f2 - 0.5) ** 2 + (f3 - 0.5) ** 2 + (f4 - 0.5) ** 2 + (f5 - 0.5) ** 2 + (f6 - 0.5) ** 2 + (f7 - 0.5) ** 2 + (f8 - 0.5) ** 2 <= 1:
                        break
        table[i][0] = "+1"
        table[i][1] = f1; table[i][2] = f2
        table[i][3] = f3; table[i][4] = f4
        table[i][5] = f5; table[i][6] = f6
        table[i][7] = f7; table[i][8] = f8

# Generates signal data in second hypersphere by randomly generating points
# in 2-radius hypercube and selecting points that fall within 2-radius
# hypersphere until 10% of total data is generated.
for i in range(int(0.1 * size), int(0.2 * size)):
        while True:
                f1 = random.uniform(-1.5, 1.5); f2 = random.uniform(-1.5, 1.5)
                f3 = random.uniform(-1.5, 1.5); f4 = random.uniform(-1.5, 1.5)
                f5 = random.uniform(-1.5, 1.5); f6 = random.uniform(-1.5, 1.5)
                f7 = random.uniform(-1.5, 1.5); f8 = random.uniform(-1.5, 1.5)
                if (f1 + 0.5) ** 2 + (f2 + 0.5) ** 2 + (f3 + 0.5) ** 2 + (f4 + 0.5) ** 2 + (f5 + 0.5) ** 2 + (f6 + 0.5) ** 2 + (f7 + 0.5) ** 2 + (f8 + 0.5) ** 2 <= 1:
                        break
        table[i][0] = "+1"
        table[i][1] = f1; table[i][2] = f2
        table[i][3] = f3; table[i][4] = f4
        table[i][5] = f5; table[i][6] = f6
        table[i][7] = f7; table[i][8] = f8

# Generates background data outside hypersphere by randomly generating
# points and selecting those that fall outside 4-radius hypersphere
# until remaining 90% of total data is generated.
for i in range(int(0.2 * size), size):
        while True:
                f1 = random.uniform(0, 10); f2 = random.uniform(0, 10)
                f3 = random.uniform(0, 10); f4 = random.uniform(0, 10)
                f5 = random.uniform(0, 10); f6 = random.uniform(0, 10)
                f7 = random.uniform(0, 10); f8 = random.uniform(0, 10)
                if (f1 - 0.5) ** 2 + (f2 - 0.5) ** 2 + (f3 - 0.5) ** 2 + (f4 - 0.5) ** 2 + (f5 - 0.5) ** 2 + (f6 - 0.5) ** 2 + (f7 - 0.5) ** 2 + (f8 - 0.5) ** 2 > 1 and\
                   (f1 + 0.5) ** 2 + (f2 + 0.5) ** 2 + (f3 + 0.5) ** 2 + (f4 + 0.5) ** 2 + (f5 + 0.5) ** 2 + (f6 + 0.5) ** 2 + (f7 + 0.5) ** 2 + (f8 + 0.5) ** 2 > 1:
                        break
        table[i][0] = "-1"
        table[i][1] = f1; table[i][2] = f2
        table[i][3] = f3; table[i][4] = f4
        table[i][5] = f5; table[i][6] = f6
        table[i][7] = f7; table[i][8] = f8

with open('Test8DTwoHypersphereHardTraining.txt', 'w') as training, open('Test8DTwoHypersphereHardTestingAll.txt', 'w') as testingall, open('Test8DTwoHypersphereHardTestingSignal.txt', 'w') as testingsignal, open('Test8DTwoHypersphereHardTestingBackground.txt', 'w') as testingbackground:
        for i in range(0, size, 2):
                training.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
        for i in range(1, size, 2):
                testingall.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
                if table[i][0] == "+1":
                        testingsignal.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")
                else:
                        testingbackground.write(table[i][0] + " 1:" + str(table[i][1]) + " 2:" + str(table[i][2]) + " 3:" + str(table[i][3]) + " 4:" + str(table[i][4]) + " 5:" + str(table[i][5]) + " 6:" + str(table[i][6]) + " 7:" + str(table[i][7]) + " 8:" + str(table[i][8]) + "\n")