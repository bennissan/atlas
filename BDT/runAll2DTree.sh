#!/bin/bash

python runbdttree.py linearhardodds.arff linearhardevens.arff Results/linearhard0518
python runbdttree.py linearsoftodds.arff linearsoftevens.arff Results/linearsoft0518
python runbdttree.py circlehardodds.arff circlehardevens.arff Results/circlehard0518
python runbdttree.py circlesoftodds.arff circlesoftevens.arff Results/circlesoft0518
python runbdttree.py twocirclehardodds.arff twocirclehardevens.arff Results/twocirclehard0518
python runbdttree.py twocirclesoftodds.arff twocirclesoftevens.arff Results/twocirclesoft0518
