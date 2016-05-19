"""
runbdt.py
Ben Nissan

Trains and tests boosted decision trees through WEKA to classify a set of provided data
with different stump counts.  Provides information useful for determining the optimal
values for these parameters: the number of false positives and negatives, as
well as the overall efficiency (or accuracy).  Note: provided data should be separated
in advance into equally-sized training and testing groups.  Further information on
this, and other uses for WEKA, can be found in the WEKA documentation.

To run: python runbdt.py trainFile testFile resultFile
"""

# Modules to interface with the command line and time the program
from subprocess import Popen, PIPE
from sys import argv
from time import time

startTime = time()

# The training and testing sets, respectively
trainFile = argv[1]
testFile = argv[2]
resultFile = argv[3]

# Size of data sets
with open(trainFile) as f:
        dataSize = sum(1 for line in f) - 7

# Tables for our information; choose stump counts as necessary
treeCounts = range(10, 1010, 10)
efficiencies = []
FPFs = []
FNFs = []

i = 1
for treeCount in treeCounts:
	# Runs BDT program through terminal command and saves output
	trainAndTest = ["../Packages/WEKA/BDTTreeWEKA", trainFile, testFile, str(treeCount)]
	output = Popen(trainAndTest, stdout = PIPE).stdout.read()
	
	# Filters out useful portions of output text
	confusionMatrix = output.split("=== Error on test data ===")[1].split("classified as")[1].split()

	# Extracts information needed from portions of output text
	FPF = float(confusionMatrix[6]) / dataSize
	FNF = float(confusionMatrix[1]) / dataSize
	efficiency = 1 - FNF
	
	# Appends information to tables
	efficiencies.append(efficiency)
	FPFs.append(FPF)
	FNFs.append(FNF)

	# Tracks progress
	print "Progress: %(current)d/%(total)d" % {"current": i, "total": len(treeCounts)}
	i += 1


# Saves results to file
with open(resultFile, "w") as results:
	j = 0
	for treeCount in treeCounts:
		line = " ".join([str(treeCount), str(efficiencies[j]), str(FPFs[j]), str(FNFs[j]), "\n"])
		results.write(line)
		j += 1


# Reports runtime
print "Total runtime: " + str(time() - startTime)
