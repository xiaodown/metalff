from pydbml import PyDBML
from pathlib import Path
from os import getcwd
import git

curr_dir = getcwd()
top_level_dir = git.Repo(curr_dir, search_parent_directories=True).working_tree_dir
parsed = PyDBML.parse_file(Path(f"{top_level_dir}/schema.dbml"))

outfile = open(f"{top_level_dir}/schema.sql", "w")
outfile.write(parsed.sql)
outfile.close()