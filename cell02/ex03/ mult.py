num1 = int(input("Enter The first number : \n"))
num2 = int(input("Enter The second number : \n"))
x = num1*num2
print(f"{num1} x {num2} = {x}\n")
if x > 0 :
    print("The result is positive.")
elif x < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
