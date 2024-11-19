import sys
if len(sys.x) < 3:
    print("none")
else:
    for value in reversed(sys.x[1:]):
        print(value)