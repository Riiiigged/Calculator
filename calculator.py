# Simple Calculator

print("Simple Calculator")
print("Operations: +  -  *  /")
print("Type 'q' to quit")

while True:
    # Ask for the first number
    first = input("\nEnter first number: ")
    if first == "q":
        break

    # Ask for the operation
    op = input("Enter operation (+, -, *, /): ")
    if op == "q":
        break

    # Ask for the second number
    second = input("Enter second number: ")
    if second == "q":
        break

    # Turn the text into numbers
    a = float(first)
    b = float(second)

    # Do the math
    if op == "+":
        print("Answer:", a + b)
    elif op == "-":
        print("Answer:", a - b)
    elif op == "*":
        print("Answer:", a * b)
    elif op == "/":
        if b == 0:
            print("Can't divide by zero!")
        else:
            print("Answer:", a / b)
    else:
        print("That's not a valid operation.")

print("Goodbye!")
