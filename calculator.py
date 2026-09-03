def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    return a / b

print("Simple Calculator")
print("Operations: add, subtract, multiply, divide\n")

while True:
    num1 = float(input("Enter first number: "))
    operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        result = "Not a valid operation"

    print(f"Result: {result}\n")

    again = input("Do another calculation? (y/n): ")
    if again.lower() != "y":
        print("See you next time")
        break