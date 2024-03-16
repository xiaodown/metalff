#!/bin/bash
current_dir=$(pwd)

# Find the top level of the git repo and move there
top_level=$(git rev-parse --show-toplevel)
cd $top_level

# Generate the requirements.in file and then compile it to requirements.txt
pipreqs --savepath=requirements.in && pip-compile

# return you to the directory you were in when you ran the script
cd $current_dir