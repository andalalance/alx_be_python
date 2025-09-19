#Learn to use Match Case statements for handling multiple operations in a simple calculator program.

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if numberTwo == 0 and operation == "/":
    print("Cannot divide by zero.")
elif operation == "+":
    result = numberOne + numberTwo
    print("The result is", result)
elif operation == "-":
    result = numberOne - numberTwo
    print("The result is", result)
elif operation == "*":
    result = numberOne * numberTwo
    print("The result is", result)
else:
    result = numberOne / numberTwo
    print("The result is", result)
