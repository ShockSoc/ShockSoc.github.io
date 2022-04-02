#!/bin/bash
set -e
pip install -r requirements.txt

python3 shock.py build

cd build/
# create a fresh new git repo in the output directory
git init
git add -A
git commit -m 'deploy'

git push -f git@github.com:ShockSoc/ShockSoc.github.io.git publish:gh-deploy
