# Greeting
print("Hello!")
name = input("What is your name? ")
print(f"Greetings, {name}")


# Number Inputs
print("This is a basic calculator that adds, subtracts, multiplies, and divides.")
first_number = float(input("First number?~~~> "))
second_number = float(input("Second number?~~~> "))


# Calculator
sum = first_number + second_number
print(f"The sum is {sum}")
difference = first_number - second_number
print(f"The difference is {difference}")
product = first_number * second_number
print(f"The product is {product}")
quotient = first_number / second_number
print(f"The quotient is {quotient:.4f}")
print("Now, we are going to convert distance from km to m.")


# Conversions
km_number = float(input("How many kilometers?~~~> "))
meters = km_number * 1000
print(f"In meters, that would be {meters}m.")
print("Have a good day!")