import sys

x = sys.argv
if len(x) > 1:
    for arg in x[1:]:
        print(arg.upper())
else:
    print("none")