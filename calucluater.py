

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)
else:

    print("Invalid operator!")
