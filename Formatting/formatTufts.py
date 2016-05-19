#!/usr/bin/python
'''
Juila Rowe
March 5, 2014

This program takes a file in libsvm format and 
converts it to the Tufts format. Modified form
Jared Moskowitz's formatScript.py

Will output a new file in the desired format.
'''

import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close
import os.path


#my_float and checkFormat functions contain code taken
#from the LIBSVM package
#see libsvm/tools/checkdata.py

# works like float() but does not accept nan and inf
def my_float(x):
        if x.lower().find("nan") != -1 or x.lower().find("inf") != -1:
                raise ValueError

        return float(x)


#given the arguments from the command line, this function
#checks to see if the given file is already of the correct format
#
#it will exit if too many arguments are given or the file given
#does not contain a dataset
#
#return 0 if already correctly formatted and 1 otherwise
def checkData(argv):
        if len(argv) != 2:
                print "Exception: incorrect number of arguments. Exp: python pythonScript.py file.txt"
                exit(1)

        dataset = argv[1]

        if not os.path.exists(dataset):
		print "Exception: not a data file. Exiting program"
                exit(1)

        line_no = 1
        error_line_count = 0
        for line in open(dataset, 'r'):
                line_error = False

                # each line must end with a newline character
                if line[-1] != '\n':
                        line_error = True

                nodes = line.split()

                # check label
                try:
                        label = nodes.pop(0)

                        if label.find(',') != -1:
                                # multi-label format
                                try:
                                        for l in label.split(','):
                                                l = my_float(l)
                                except:
                                       line_error = True
                        else:
                                try:
                                        label = my_float(label)
                                except:
                                        line_error = True
                except:
                        line_error = True

                # check features
                prev_index = -1
                for i in range(len(nodes)):
                        try:
                                (index, value) =  nodes[i].split(':')

                                index = int(index)
                                value = my_float(value)

                                # precomputed kernel's index starts from 0 and LIBSVM
                                # checks it. Hence, don't treat index 0 as an error.
                                if index < 0:
                                        line_error = True
                                elif index <= prev_index:
                                        line_error = True
                                        prev_index = index
                        except:
                                line_error = True

                line_no += 1

                if line_error:
                        error_line_count += 1

        if error_line_count > 0:
                return 1
        else:
                return 0



#Given a file path, this method will go through
#and convert the contents to the desired format
def format(file_path):
        #Create new file
        fh, abs_path = mkstemp()
        new_file = open(abs_path,'w')
        old_file = open(file_path, 'r')        

	#skip the header
	count = 0
	while count < 9:
		arr = old_file.readline()
		count = count + 1
        #perform all non header lines
	for line in old_file:
                arr = line.split()
		new_arr = list()
		i = 0
                #remove classifier from beginning
                classifier = arr.pop(0)
		#format the class data
		while i < len(arr) :
			parsed = arr[i].split(":")
			if int(parsed[0])-1 != i :
				new_arr.append('0.0')
				arr.reverse()
				arr.append('0.0')
				arr.reverse()
			else :
				new_arr.append(parsed[1])
			i += 1
                #correctly format classifier
                if classifier == '+1' :
                	classifier = classifier.replace("+", "")
                
                classifier = classifier + '.'
               	new_arr.append(classifier)

                new_line = " ".join(new_arr)
		print(new_line)
                #write newly formatted line
                #new_file.write(new_line)

#need to change this to write to a new file
        #close temp file
        new_file.close()
        close(fh)
        old_file.close()
        #Remove original file
        #Remove original file
        #remove(file_path)
        #Move new file
        #move(abs_path, file_path)
        #print "Successfully formatted file " + file_path
        exit(0)


def main():
        #check to see if data has been formatted
        if checkData(sys.argv) == 0:
                print "Exception: Input file incorrectly formatted."
                exit(1)

        #format data and overwrite file
        format(sys.argv[1])


if __name__ == "__main__":
        exit(main())        

