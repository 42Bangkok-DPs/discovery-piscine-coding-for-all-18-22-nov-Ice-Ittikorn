import sys
if len(sys.argv) != 2:
    print("none")
else:
    parameter = sys.argv[1]
    user = input("What was the parameter? ")
    if user == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")