#!/bin/bash

python runbdtstump.py linearhardodds.arff linearhardevens.arff ResultsStump/linearhard0519
python runbdtstump.py linearsoftodds.arff linearsoftevens.arff ResultsStump/linearsoft0519
python runbdtstump.py circlehardodds.arff circlehardevens.arff ResultsStump/circlehard0519
python runbdtstump.py circlesoftodds.arff circlesoftevens.arff ResultsStump/circlesoft0519
python runbdtstump.py twocirclehardodds.arff twocirclehardevens.arff ResultsStump/twocirclehard0519
python runbdtstump.py twocirclesoftodds.arff twocirclesoftevens.arff ResultsStump/twocirclesoft0519
