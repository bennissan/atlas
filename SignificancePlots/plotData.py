#!/usr/bin/python
'''
plotData.py

Jared Moskowitz & Julia Rowe
05/07/15


USAGE: python plotData.py Scores.txt 

'''


import sys, io
from scipy.io.arff import loadarff
import scipy.spatial.distance as pyDistance
import random
import numpy as np
import pylab as plt
import math


#define bin sizes for histogram
bins = 40


def main():
        #read in data
        signalData, backgroundData = read_scores(sys.argv[1])

        #plot data
        plotData(signalData, backgroundData)

        exit(1)


def plotData(sigData, backData):
        
        treeCount = sys.argv[2]

        #plot histogram of distances from hyperplane
        myplt = plt.figure(1)
        plt1 = plt.subplot(211)
        plt1.set_ylabel('Frequency')
        signalHistInfo = plt.hist(sigData, bins, alpha=0.5, histtype='stepfilled', label='x')
        backgroundHistInfo = plt.hist(backData, bins, alpha=0.5, histtype='stepfilled', label='y')
        plt.axis([-22, 5, 0, 1500])
        plt.title('Weighted Tree Scores For ' + str(treeCount) + ' Classifiers')

        plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=0.4)
        stackedHistBins, bin_edges, patches = plt.hist((sigData,backData), bins, alpha=0, label='x', histtype='barstacked')
        cutValues = getCutInfo(stackedHistBins)

        #plot significance graph
        plt2 = plt.subplot(212)
        plt2.set_ylabel('Signal / sqrt(background)')
        plt2.set_xlabel('Boosting Output')

        bin_edges = np.delete(bin_edges, -1)
        plt.axis([-22, 5, 0, 70])
        plt.plot(bin_edges,cutValues)
        plt.savefig(str(treeCount) + ' TreeHist.png')
        plt.show()



def read_scores(fileName):
    lines = [line.rstrip('\n') for line in open(fileName)]
    signal = list()
    background = list()
    for line in lines:
        tempArr = line.split()
        if(tempArr[1] == "-1"):
            background.append(float(tempArr[0]))
        else:
            signal.append(float(tempArr[0]))

    return signal, background

'''
Takes in an array of size two that contains two arrays.
These correspond to the bins of signal and background for a
stacked histogram. What is returned is data in an array that is
s/b^(0.5)
'''
def getCutInfo(bins):
        signif = list()
        sigBins = bins[0].tolist()
        backBins = bins[1].tolist()

        #calculate cut for each bin
        for i in range(len(sigBins)):
                backSum = 0
                sigSum = 0
                #sum all bins past and including cut
                for j in range(i, len(sigBins)):
                        sigSum += sigBins[j]
                        backSum += backBins[j]
                signifNum = sigSum/math.sqrt(backSum)
                signif.append(signifNum)
        return signif



if __name__ == "__main__":
        exit(main())
