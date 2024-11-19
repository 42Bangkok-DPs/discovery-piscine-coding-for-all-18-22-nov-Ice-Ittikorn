import sys
if len(sys.argv) <2 :
    print("none")
else:
    for arg in sys.argv:
        if not arg.endswith("ism"):
            print(f"{arg}ism")