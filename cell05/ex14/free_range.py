import sys
if len(sys.argv) != 2:
    print("none")
else:
    print(" ".join(str(i) for i in range(start, end + 1)))