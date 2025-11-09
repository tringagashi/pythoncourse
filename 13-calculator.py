def calculator():
    print("Simple Calculator")

    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operation!")

calculator()
