import sys
if len(sys.argv) <2 :
    print("none")
else:
    for arg in args:
        if not arg.endswith("ism"):
            print(f"{arg}ism")