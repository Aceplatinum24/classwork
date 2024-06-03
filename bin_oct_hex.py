# Number Inputs
num1 = int(input("Give me an integer? "))
num2 = int(input("Give me another integer? "))


# Primary Numbers
print(f"Your first number in binary is {num1:b}.")
print(f"Your first number in octal is {num1:o}.")
print(f"Your first number in hexadecimal is {num1:x}.")


# Secondary Numbers
print(f"Your second number in binary is {num2:b}.")
print(f"Your second number in octal is {num2:o}.")
print(f"Your second number in hexadecimal is {num2:x}.")


# Sum of Both Numbers
sum = num1 + num2
print(f"The sum of your two numbers in decimal is {sum}.")
print(f"The sum of your two numbers in binary is {sum:b}.")
print(f"The sum of your two numbers in octal is {sum:o}.")
print(f"The sum of your two numbers in hexadecimal is {sum:x}.")

