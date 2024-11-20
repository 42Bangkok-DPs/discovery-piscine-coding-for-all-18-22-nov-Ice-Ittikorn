num = int(input("Enter a number less than 25\n"))
if num > 25:
    print("eror")
else :
    print(f"Inside the loop, my variable is {num}")
    while num < 25:
        num +=1
        print(f"Inside the loop, my variable is {num}")