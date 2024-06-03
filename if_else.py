# Time Data
import time
def delay_print(s):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(0.03)


# Definitions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b


# Greeting
delay_print("Hello! \n")
name = input("What is your name? ")
delay_print(f"Greetings, {name} \n")


# Number/Operation
num1 = float(input("First number? "))
num2 = float(input("Second number? "))

operation = input("""Pick an operation. Your choices are: 
Add (+), Subtract (-), Multiply (*), Divide (/): """)


# Mathematics
if operation == "+":
    result = add(num1, num2)
    operation_label = "sum"
elif operation == "-":
    result = subtract(num1, num2)
    operation_label = "difference"
elif operation == "*":
    result = multiply(num1, num2)
    operation_label = "product"
elif operation == "/":
    result = divide(num1, num2)
    operation_label = "quotient"
else:
    result = "Invalid operation"
    operation_label = ""


# Display Results
if operation_label:
    print(f"The {operation_label} is:", result)


