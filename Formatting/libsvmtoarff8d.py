from sys import argv

fileName = argv[1]

f1s = []; f2s = []; f3s = []; f4s = []; f5s = []; f6s = []; f7s = []; f8s = []; classes = []

with open(fileName, "r") as initial:
        for line in initial:
                splitLine = line.split()
                classes.append(int(splitLine[0]))
                f1s.append(splitLine[1].split(":")[1])
                f2s.append(splitLine[2].split(":")[1])
                f3s.append(splitLine[3].split(":")[1])
                f4s.append(splitLine[4].split(":")[1])
                f5s.append(splitLine[5].split(":")[1])
                f6s.append(splitLine[6].split(":")[1])
                f7s.append(splitLine[7].split(":")[1])
                f8s.append(splitLine[8].split(":")[1])

with open(fileName + ".arff", "w") as converted:
        converted.write("@RELATION %s.txt\n\n" % fileName)
        converted.write("@ATTRIBUTE f1 numeric\n")
        converted.write("@ATTRIBUTE f2 numeric\n")
        converted.write("@ATTRIBUTE f3 numeric\n")
        converted.write("@ATTRIBUTE f4 numeric\n")
        converted.write("@ATTRIBUTE f5 numeric\n")
        converted.write("@ATTRIBUTE f6 numeric\n")
        converted.write("@ATTRIBUTE f7 numeric\n")
        converted.write("@ATTRIBUTE f8 numeric\n")
        converted.write("@ATTRIBUTE class {1, -1}\n\n")
        converted.write("@DATA\n")
        for i in range(len(classes)):
                converted.write(f1s[i] + "," + f2s[i] + "," + f3s[i] + "," + f4s[i] + "," + f5s[i] + "," + f6s[i] + "," + f7s[i] + "," + f8s[i] + "," + str(classes[i]) + "\n")