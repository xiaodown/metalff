#!/bin/bash
top_level=git rev-parse --show-toplevel
cd $top_level
pipreqs --savepath=requirements.in && pip-compile
