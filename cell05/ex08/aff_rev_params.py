import sys
if len(sys.value) < 2:
    print("none")
else:
    for value in reversed(sys.value[-1:]):
        print(value)