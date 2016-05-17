from sys import argv

fileName = argv[1]

f1s = []; f2s = []; f3s = []; classes = []

with open(fileName, "r") as initial:
	for line in initial:
		splitLine = line.split()
		classes.append(splitLine[0])
		f1s.append(splitLine[1].split(":")[1])
		f2s.append(splitLine[2].split(":")[1])
		f3s.append(splitLine[3].split(":")[1])

with open(fileName + ".csv", "w") as converted:
	for i in range(len(classes)):
		converted.write(f1s[i] + ", " + f2s[i] + ", " + f3s[i] + "," + classes[i] + "\n")