# ###########################   
# # invalid variable names: #   
# ###########################

# ## These four examples will cause errors ensure they are 
#     commented out before you move on.

# ## Can't use keywords, as an example: 
# if = 6

# ## Can't start with number
# 3rdthing = "hi"

# ## Can't have spaces inside of the name
# my var = 3

# ## Can't have special characters (only "_" is allowed inside a variable name)
# $d = 6

# #########################   
# # valid variable names: #   
# #########################

# mynumber = 7
# temp_in_f = 8.3
# my2ndthing = "hi"
# x3 = "stuff"
# _myStuff = 7
# result = mynumber * _myStuff

# ## Using the variables: 
# print(mynumber)
# print(f"The recorded temperature is {temp_in_f}°F")
# print(f"The following message was received '{my2ndthing}'.")
# print(f"The result of multiplying", mynumber, "and", _myStuff, "is equal to", result)

# ## This definition of a variable is valid, but please don't, 
# because "input" will no longer be a function.
# input = 7

## When importing modules, there are a few approaches you can use:
# import math
# print(math.sqrt(5))

# from math import sqrt
# print(sqrt(5))

# import math as m
# print(m.sqrt(5))

# from math import *
# print(sqrt(5))

## Example group 1
## Try these all at once.
# item_number = 27.283
# print()
# print(f"My item num is {item_number}.")
# print()
# print(f"My item num is {item_number:10}. Notice that it is padded with spaces on the left.")
# print()
# print(f"My item num is {item_number:.2f}, rounded to two decimal places.")
# print()
# print(f"My item num is both rounded and has extra space: {item_number:9.2f}. Do you see?")
# print()
# print("You can also center the value within the available space.")
# print("I'll add some letters before and after to make it clear:")
# print(f"letters{item_number:^11.2f}letters")
# print()
# print(f"Here's how to left-align with some letters after for visual context: {item_number:<11.2f}letters")

## Example group 2
## Try these all at once.
# another_num = 17
# print("Here's how to display in binary, octal, hexadecimal:")
# print(f"The number {another_num}, expressed in binary, is {another_num:b}.")
# print(f"The number {another_num}, expressed in octal, is {another_num:o}.")
# print(f"The number {another_num}, expressed in hexadecimal, is {another_num:x}.")

## Incidentally, the format code "d" means decimal, which is the default:
# print(f"The number {another_num}, expressed in decimal, is {another_num:d}.")

## You can also display the number with a prefix that indicates the number system:
# print(f"The number {another_num}, expressed in binary with a prefix, is {another_num:#b}.")
# print(f"The number {another_num}, expressed in octal with a prefix, is {another_num:#o}.")
# print(f"The number {another_num}, expressed in hexadecimal with a prefix, is {another_num:#x}.")

## Note that the format specifiers for other number systems don't work for floats:
# item_number = 27.283
# print(f"This will give an error, because item_number is a float: {item_number:b}.")

## 1
## Ask the user a number.
## Display the number rounded to 3 decimal places.

# print("Let's try something ")
# num = float(input("Choose a number! "))
# print(f"Your number rounded to 3 decimal places is {num:.3f}")


## 2 
## Ask the user for the current cost-per-gallon of
## gasoline. Display the cost per pint,
## rounded to the nearest cent.

# cpg = float(input("GOG cost? $"))
# cost = cpg / 8
# print(f"COG per pint is ${cost}")
