import sys
if len(sys.agev) < 3:
    print("none")
else:
    for value in reversed(sys.agev[1:]):
        print(value)