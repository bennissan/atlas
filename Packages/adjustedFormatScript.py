

#!/usr/bin/python
'''
Jared Moskowitz
01/16/15

This file takes in a file path formatted in our own
way and converts it to a format compatible with the
libsvm package.

The given file will be overwritten.
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
	if len(argv) <= 2:
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
def format(file_path, class_value):
        #Create temp file
        fh, abs_path = mkstemp()
        new_file = open(abs_path,'w')
        old_file = open(file_path)

        #perform on every line
        for line in old_file:
                attr = 1;
                arr = line.split()
                #format the class data
                for i in range(len(arr) - 1):
                        arr[i] = str(i + 1) + ":" + arr[i]
                #remove -1. or +1. from end
                classifier = arr.pop()

                #insert +1 or -1 at beginning
                classifier = classifier.replace(".", "")
                arr.insert(0, class_value)

                arr.append('\n')
                new_line = " ".join(arr)
                
                #write newly formatted line
                new_file.write(new_line)
        #close temp file
        new_file.close()
        close(fh)
        old_file.close()
        #Remove original file
        remove(file_path)
        #Move new file
        move(abs_path, file_path)
        print "Successfully formatted file " + file_path
        exit(0)


def main():
        #check to see if data has been formatted
        if checkData(sys.argv) == 0:
                print "Exception: Given file is already formatted. Exiting program."
                exit(1)

        #format data and overwrite file
        format(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
	exit(main())


