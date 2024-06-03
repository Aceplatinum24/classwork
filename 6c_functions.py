# ## 1
# ## Try this.
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# sayWelcome()
# sayWelcome()

# ## The first line, def sayWelcome(), means "Define a function named sayWelcome(). 
# ## The next three print lines are called the "body" of the function. 
# ## Just as with if, while, and for statements, you must indent the body of the 
# ## function so that Python knows what is inside the function and what is not.
# ## The last two lines are simply sayWelcome(). 
# ## Those are the lines that call (or run) the function. Let's experiment:

# ## 2
# ## Try this. How many times does it display the welcome text?
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# sayWelcome()
# sayWelcome()
# sayWelcome()


# ## 3
# ## Try this. How many times does it display the welcome text?
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# ## 4
# ## Try this. Does it display in the order that you expect?
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# def sayBye():
#     print("Goodbye, have a good day!")

# sayBye()
# sayWelcome()


# ## 5
# ## Copy and modify the previous example to make
# ## it call sayWelcome before it calls sayBye.


# ## 6
# ## Try this. Why doesn't it work?
# ## How could you define a function so that this will run?
# sayCoolStuff()

# ## 7
# ## This is an example showing where to position function definitions.
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# print("""This line of code is not well positioned -- it comes between 
#       two function definitions.""")

# def sayBye():
#     print("Goodbye, have a good day!")

# print("""This line of code is well positioned, because it comes after the 
#       function definitions.""")

# ## 8a
# ## Try this.
# def sayHiTo(name):
#     print(f"Hello {name}. Welcome to the Python course.")

# sayHiTo("Bob")
# sayHiTo("Sue")
# sayHiTo("Tom")

# ## 8b
# ## Try this.
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob", "cat")
# tellAbout("Sue", "dog")
# tellAbout("camel", "Tom")


# ## 9
# ## Copy and modify the previous example so that
# ## Tom has a pet camel, rather than vice versa.

# ## 10
# ## Try this. It will give an error message.
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob")


# ## 11
# ## Copy and modify the previous example so that Bob has a pet animal.

# ## 12
# ## Try this.
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# na = "Bob"
# ani = "cat"
# tellAbout(na, ani)

# ## 13
# ## Copy and modify the previous example so that `na` and `ani` are set by user input.

# ## 14
# ## Try this.
# def sayLengthOfEach(names):
#     for name in names:
#         print(f"The length of {name} is {len(name)}")

# sayLengthOfEach(["Bob", "Joseph", "Susan"])

# ## 15
# ## Try this.
# def convertHoursToMinutes(hours):
#     return hours * 60

# h = int(input("Give a number of hours, and I'll convert it to minutes."))
# m = convertHoursToMinutes(h)
# print(f"That would be {m} minutes.")

# ## 16
# ## Try this.
# print(convertHoursToMinutes(2))

# ## 17
# ## Try this.
# assert convertHoursToMinutes(2) == 119

# # When you run that, it should say AssertionError. 
# # (If it shows anything else, ask an instructor.)
# # To fix that test, we would write assert convertHoursToMinutes(2) == 120. 
# # If you fix it, 
# # you'll notice that it produces no output. That's to be expected.

# ## 18
# ## Define a function that converts from feet to yards.
# ## Use this structure:
# def convertFeetToYards(feet):
#     return _____

# print(convertFeetToYards(5))

# ### Practice ###
# ## 19
# ## Write two `assert` statements to check that 
# # convertFeetToYards is working correctly.