import sys
if len(sys.argv) != 2:
    print("none")
else:
    search = sys.argv[1]
    count_z = search.count('z')
    if count_z == 0:
        print("none")
    else:
        print('z' * count_z)