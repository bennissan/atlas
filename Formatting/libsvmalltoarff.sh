#!/bin/bash

python libsvmtoarff2d.py linearhardodds
python libsvmtoarff2d.py linearhardevens
python libsvmtoarff2d.py linearsoftodds
python libsvmtoarff2d.py linearsoftevens

python libsvmtoarff2d.py circlehardodds
python libsvmtoarff2d.py circlehardevens
python libsvmtoarff2d.py circlesoftodds
python libsvmtoarff2d.py circlesoftevens

python libsvmtoarff2d.py twocirclehardodds
python libsvmtoarff2d.py twocirclehardevens
python libsvmtoarff2d.py twocirclesoftodds
python libsvmtoarff2d.py twocirclesoftevens

python libsvmtoarff3d.py twospherehardodds
python libsvmtoarff3d.py twospherehardevens
python libsvmtoarff3d.py twospheresoftodds
python libsvmtoarff3d.py twospheresoftevens

python libsvmtoarff3d.py twospherehard100kodds
python libsvmtoarff3d.py twospherehard100kevens
python libsvmtoarff3d.py twospheresoft100kodds
python libsvmtoarff3d.py twospheresoft100kevens