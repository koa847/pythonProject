import sys

f_name = "bakery.csv"
args = sys.argv[1:]
if not args:
    with open(f_name, 'r', encoding="utf-8") as f:
        for str in f:
            print(str)
else:
    if len(args) == 1:
        with open(f_name, 'r', encoding="utf-8") as f:
            i = 0
            for str in f:
                if i >= int(args[0]) - 1:
                    print(str)
                i += 1
    if len(args) == 2:
        with open(f_name, 'r', encoding="utf-8") as f:
            i = 0
            for str in f:
                if i >= int(args[0]) - 1 and i < int(args[1]):
                    print(str)
                i += 1