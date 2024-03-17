#!/bin/bash

current_dir=$(pwd)

if [[ ! "$VIRTUAL_ENV" != "" ]] ;then
    echo "Must be run in a python3 venv"
    exit 1
fi

# Find the top level of the git repo and move there
top_level=$(git rev-parse --show-toplevel)
cd $top_level
rm requirements.txt 2>/dev/null

if ! command -v pipreqs &> /dev/null ;then
    echo "pipreqs not found, attempting to install..."
    pip install pipreqs >/dev/null 2>&1
fi

if ! command -v pip-compile &> /dev/null ;then
    echo "pip-compile not found, attempting to install pip-tools..."
    pip install pip-tools >/dev/null 2>&1
fi

# Generate the requirements.in file and then compile it to requirements.txt
echo "Generating requirements..."
pipreqs --savepath=requirements.in 2>/dev/null && pip-compile 2>/dev/null

echo "Done."
# return you to the directory you were in when you ran the script
cd $current_dir
