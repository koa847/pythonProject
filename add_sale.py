import sys
import os.path

args = sys.argv[1]

f_name = "bakery.csv"
if os.path.isfile(f_name):
    with open(f_name, "a", encoding="utf-8") as f:
        f.write(f'{args}\n')
else:
    with open(f_name, "w", encoding="utf-8") as f:
        f.write(f'{args}\n')
