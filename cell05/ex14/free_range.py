import sys
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print(" ".join(str(i) for i in range(start, end + 1)))