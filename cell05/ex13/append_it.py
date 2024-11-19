import sys
if not args:
    print("none")
else:
    for arg in args:
        if not arg.endswith("ism"):
            print(f"{arg}ism")