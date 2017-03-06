#!/bin/bash
for Training in *Training*.txt
do
        type=$(echo $Training | awk -F"Training.txt" '{print $1}')
        TestingAll=$type"TestingAll"
        TestingSignal=$type"TestingSignal"
        TestingBackground=$type"TestingBackground"
        
        for Testing in $TestingAll $TestingSignal $TestingBackground
        do
                sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM $Training $Testing".txt" Results/03-06/$Testing"0306.txt"
        done
done