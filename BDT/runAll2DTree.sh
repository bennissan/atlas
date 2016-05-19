#!/bin/bash

python runbdttree.py linearhardodds.arff linearhardevens.arff ResultsTree/linearhard0519
python runbdttree.py linearsoftodds.arff linearsoftevens.arff ResultsTree/linearsoft0519
python runbdttree.py circlehardodds.arff circlehardevens.arff ResultsTree/circlehard0519
python runbdttree.py circlesoftodds.arff circlesoftevens.arff ResultsTree/circlesoft0519
python runbdttree.py twocirclehardodds.arff twocirclehardevens.arff ResultsTree/twocirclehard0519
python runbdttree.py twocirclesoftodds.arff twocirclesoftevens.arff ResultsTree/twocirclesoft0519