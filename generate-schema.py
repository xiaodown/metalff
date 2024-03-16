from pydbml import PyDBML
from pathlib import Path

parsed = PyDBML.parse_file(Path("schema.dbml"))
# print(parsed.sql)

outfile = open("schema.sql", "w")
outfile.write(parsed.sql)
outfile.close()