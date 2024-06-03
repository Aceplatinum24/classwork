## 1 
## Try this.
# print("Here we go!")

## 1b
## Try this.
# print("I can print")
# print("more than one line.")

## 2a
## Try this.
# print("If you want \n separate lines, you \n can also do it \n like this.")

## 2b
# ## Try this.
# print("This thing inside quotes is called a \"string\". If you want")
# print("to put quotes inside of quotes, you precede the quotes with a backslash.")

## 2c
## Try this.
# print("""If you put three quote marks, 
# you can easily enter a
# multi-line
# string.""")

## 2d
## You can also use triple quotes similarly to how you use comments:
# print("""If I wanted to write a long explanation,
# I could write it like this
# instead of using the '#' if I wanted to.""")

## 2e
## Try this.
# print('In Python, the single quote can be used instead of the double quote.')
# print("You can put 'single quotes' inside of double quotes, or vice versa, without needing an escape sequence.")
# print('However, if you want single quotes inside of single quotes, you\'ll need to escape them using a backslash.')

## 3a
## Try this.
## firstn and lastn are the two variables in this example.
## When you run this, you won't see Smith. Why not?

# firstn = "Bob"
# lastn = "Smith"
# print(firstn)

## 3b
## Copy and modify the previous example so that it
## prints firstn, and then prints lastn.

## 4a
## Try this.
## This example uses an f-string. The f stands for "format".
## f-strings are used to insert variables inside of a string.
# firstn = "Bob"
# lastn = "Smith"
# print(f"My name is {firstn} {lastn}")

## 4b
## You can also use commas, but only in functions that
## support it, such as print.
## (Later, when we get to file writing, the 
## comma approach doesn't work, but f-strings do work.)
# print("My name is", firstn, lastn)

## (Remember to define your variables.  Where should the variable definitions be placed to be effective?)

# input("Please type your name? ")
# name = input("Please type your name? ")
# print(f"Hello {name}!")

## 4c
## Try this.
## When you run it, it will ask you to type something.
## You will need to click inside the terminal on the bottom half of the screen
##   so that it has "focus" (that is, you want the words you type
##   to be entered in the terminal).
# print("Hello!")
# cartype = input("Type the name of a car, then press enter: ")
# print(f"The car you named is {cartype}. That was a good choice.")

## 4d
## Copy and modify the previous example so that it asks the user for the name of a car,
## and then prints "The car you named is ____. Do you have one?"
## In the blank, you should include whatever car the user named.
## Example run 1:
##   Type the name of a car: ✎ Honda
##   The car you named is Honda. Do you have one?
## Example run 2:
##   Type the name of a car: ✎ Ford
##   The car you named is Ford. Do you have one?
## (The "✎" emoji is optional. It indicates where the user
##  will enter input.)

# print("Hello!")
# cartype = input("Type the name of a car, then press enter: ")
# print(f"The car you named is ✎ {cartype}. Do you have one?.")

## 4e
## Copy and modify the previous example so that it asks the user for the name of an animal,
## and then prints "The animal you named is ____. I think that it would make a nice pet."
## Example run:
##   Type the name of an animal: ✎ dog
##   The animal you named is dog. I think that it would make a nice pet.

## (Questions marked as INSTRUCTOR-CHECK are ones for which you should
##  show your answer to an instructor to verify that it fulfills the intent of the question.)

## 5
## Try this.
# firstn = input("Please enter a first name? ")
# lastn = "Smith"
# print(f"Maybe someone is named: {firstn} {lastn}.")

## 6a
## Copy and modify the previous example so that it matches this:
## Example run:
##   First name? ✎ Bob
##   Last name? ✎ Smith
##   Your name is Bob Smith.

## 7
## Make a program that produces these results:
## Example run 1:
##   Favorite color? ✎ red
##   red is a pretty color.
## Example run 2:
##   Favorite color? ✎ blue
##   blue is a pretty color.

######################################################
# print("Hello!")
# color = input("What is your favorite color? ")
# print(f"{color} is a pretty color")
# while True:
#     user_input = input("Do you have another color you like? (yes/no): ")
#     if user_input.lower() in ["yes", "y"]:
#         color2 = input("What is your next favorite color? ")
#         print(f"{color2}, That's a horrible color!")
#         break
#     elif user_input.lower() in ["no", "n"]:
#         print("You suck at life")
#         break
#     else:
#         print("Invalid input. Please enter yes/no.")
#######################################################

## 8
## Ask the user for the name of an animal and of a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant the user entered.

# print("Continue....")
# animal = input("Name an animal")
# plant = input("Name a plant")
# print(f"The {animal} eats {plant} every day")

## 9a
## Try this.
# a = "Hello"
# b = "Goodbye"
# c = a + b
# print(c)

## 9b
# mysentence = "Hello" + "everyone"
# print(mysentence)

## 9c
## Copy and modify the previous example so that 
## it displays a space: "Hello everyone" rather than "Helloeveryone".

# mysentence = "Hello " + "everyone"
# print(mysentence)

## 10
## Try this.
# a = input("First word? ")
# b = input("Second word? ")
# c = a + b
# print(c)

## 11
# a = 5
# b = 3
# c = a + b
# print(c)

## 12
# a = "5"
# b = "3"
# c = a + b
# print(c)

## 13 
# print("Welcome to the number adder that doesn't work right!")
# a = input("What's a number you like? ")
# b = input("Can you give me another number you like? ")
# c = a + b
# print("I added them. Here's what I got...")
# print(c)

## 14
## Try this.  It will perform proper arithmetic.
# print("Welcome to the number adder that works well!")
# a = int(input("What's a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

## 15
## Try this. You will get an error. How do you fix it?
# a = int(input("What is a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

## 16
## Try this. You will get an error. How do you fix it?
# favnum = int(input("What is your favorite number? "))
# onemore = favnum + 10
# print(f"One more would be {onemore}")

## 17
## Ask the user for an integer.
## Display "That number plus 2 is ___".
# integer = int(input("Think of a number! "))
# twomore = integer + 2
# print(f"That number plus 2 is {twomore}")

## 18
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".
# print("Gimme 2 numbers, any numbers and I will multiply them for you")
# a = int(input("What's the first number? "))
# b = int(input("Now, give me your second number--> "))
# c = a * b
# print(f"By the power of coding, your answer is...{c}")

########################
## LUNCH BREAK (5-22) ##
########################

## 19
## Ask the user for two integers.
## Display "The first number minus the second number is ___".

# print("Gimme 2 numbers, any numbers and I will subtract them for you")
# a = int(input("What's the first number? "))
# b = int(input("Now, give me your second number--> "))
# c = a - b
# print(f"By the power of coding, your answer is...{c}")

## 20
## Ask the user for a number.
## Display "Half of that number is ___".

# print("Gimme 2 numbers, any numbers and I will divide them for you")
# a = int(input("What's the first number? "))
# b = int(input("Now, give me your second number--> "))
# c = a / b
# print(f"By the power of coding, your answer is...{c}")

## 21a
## Try this.
# print("Hello"*3)

## 21b
## Copy and modify the previous example to ask the user for a string.
## Display whatever string the user enters three times 
##  (using *3, as in the previous example).

## 22a
## Try this. It will give an error.
# print("Hello" * "3")

## 22b
## Copy and modify the previous example to ask the user for both the
## string to be multiplied and the number of repetitions.
## Hint: If you get an error, is it the same error as in the `print("Hello" * "3")` example? If so, why?

## 23
## Does this example do what you expect?
## Why does it repeat the number five times rather than doing "real" math multiplication?
## How do you make it do math?
# num = input("Give me a number. ")
# print("I'm going to try to multiply that number by 5,")
# print("but something strange is going to happen:")
# print(num*5)

# a = int(input("Give me a number... "))
# print("I'm going to try to multiply that number by 5,")
# b = a * 5
# print(f"You got...{b}")

## 24
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)

# a = int(input("how many did you get right? "))
# b = int(input("how many questions were on the test? "))
# c = a / b
# d = c * 100
# print(f"You got...{d}%")

## 25
## Ask the user for name and age.
## Display "Guess what, ___, in two years you'll be ___."
## (The user-provided name goes in the first blank, and the
##   age two years from now in the second blank.)

# name = input("What is your name? ")
# age = int(input("What is your age? "))
# age2 = age + 2
# print(f"Guess what, {name}, in two years you'll be {age2}.")

## 26 
##Duplicating/repeating a string
## In the current example, the data type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply an integer times an integer?
## What about a string times an integer?
# x = 123
# y = "123"
# print(x*3)
# print(y*3)

## 27
## Try this. It shows how to use the type() function.
## `x` and `y` are both variables, are they integers or strings?
# x = input("Word ")
# y = int(input("5 "))
# print(f"The type of x is {type(x)}, which is another way to say 'string'.")
# print(f"The type of y is {type(y)}, which is another way to say 'integer'.")
# print(x*y)

## 28a
## Determine the type of each of these variables (integer, string, or something else).
## Hint: Python can tell you the types using the type() function.
### 26 Duplicating/repeating a string
## Try this.
## In the current example, the data type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply an integer times an integer?
## What about a string times an integer?

## 28a
## Determine the type of each of these variables (integer, string, or something else).
## Hint: Python can tell you the types using the type() function.
# mystery = 6
# another = "Hello"
# something = input("Enter a number.")
# whatIsThis = int(input("Enter a number."))
# thisIsSomething = 3.11
# print(f"{type(mystery)}, {type(another)}, {type(something)}, {type(whatIsThis)}
#       {type(thisIsSomething)}")

## 28b
# somenum = int(input("""Try typing a non-whole number, such as an approximate value for pi. 
#                     You'll see that it doesn't work: """))
# print(f"You typed {somenum}")

## 28c
## Try this. You'll see that it allows for non-whole numbers.
# somenum = float(input("Try typing another non-whole number: "))
# print(f"You typed {somenum}")

## 28d
## Ask the user for two numbers.
## Use float() in the places where you would use int().
## Display "The sum of your two numbers is ___".

## 28e
## Ask the user for a number, making sure that you allow for non-whole numbers.
## Display "Twice that number is ___".
## Example run:
##    Can you give me a number? 3.4
##    Twice that number is 6.8

## 28f
## For extra practice with floats, copy and modify some of your previous exercises
##   so they use float instead of int.

## 29
## Try this. You will get an error. Why?
## (Note: This isn't fixable. It's a purely educational question.)
# x = "hello"
# y = "goodbye"
# print(x*y)

## 30
## Try this. You will get an error. Why?
## (Note: no need to try to fix this. It's a purely educational question.)
# x = "3"
# y = "5"
# print(x*y)

