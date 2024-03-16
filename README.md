## Fantasy Football, but instead it's metal musicians

### Install instructions

Oh god, we're not there yet.

#### Generate requirements

Run the script `./generate-requirements.sh` to create requirements.txt

Then create a venv, and `pip install -r requirements.txt`.  

Made using python3.11; probably requires something like python3.8+.


#### Generate schema

Inside the venv, run `python generate-schema.py` which will output schema.sql