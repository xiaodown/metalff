## Fantasy Football, but instead it's metal musicians

### Install instructions

Oh god, we're not there yet.

#### Generate requirements

Run the script `.scripts/generate-requirements.sh` to create requirements.txt

Then create a venv, and `pip install -r requirements.txt`.

Made using python3.11; probably requires something like python3.8+.


#### Generate schema

Inside the venv, run `python scripts/generate-schema.py` which will output schema.sql


#### Settings

Copy `settings.py.example` to `settings.py` and edit as needed. (not future proof)
