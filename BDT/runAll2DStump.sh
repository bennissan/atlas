#!/bin/bash

python runbdtstump.py linearhardodds.arff linearhardevens.arff Results/linearhard0518
python runbdtstump.py linearsoftodds.arff linearsoftevens.arff Results/linearsoft0518
python runbdtstump.py circlehardodds.arff circlehardevens.arff Results/circlehard0518
python runbdtstump.py circlesoftodds.arff circlesoftevens.arff Results/circlesoft0518
python runbdtstump.py twocirclehardodds.arff twocirclehardevens.arff Results/twocirclehard0518
python runbdtstump.py twocirclesoftodds.arff twocirclesoftevens.arff Results/twocirclesoft0518
