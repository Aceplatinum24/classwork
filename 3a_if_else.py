## 1
## Try this. Run it more than once.
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")


## 1b
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.


## 1c
## Try this. Run it a few times.
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")


## 1d
## Copy and modify the previous example so that the computer
## will pick numbers between 7 and 10 instead.


## 1e
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"


## 2
## Try this.
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.") 
     

## 3
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.


## 3b
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand."


## 3c
## Try this.
## Notice that the "Have a good day" line prints regardless of
## the chosen name.  This is because it is
## not indented (it has no spaces before the line).
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Hello Joe!")
#     print("Your name rhymes with low.")
# print("Have a good day.")

## 4
## Try this.
# import random
# age = random.randint(18, 24)
# print(f"Pretend that you are {age} years old.")
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

## 5
## Copy and modify the above example so that the
## legal drinking age is 40. (Just to be funny.) 

## 6
## Try this. Notice that it will ask for input. 
# thename = input("What is your name? ")
# if thename == "george":
#     print("Are you named after the first US President?")
# else:
#     print("Hello.")

## 6b
## Change the previous example so that if the
## user types "bob", it will reply "Are you the painter?"

## 6c
## Try this.
# name = input("What is your name? ") 
# if name == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.") 
    
 
## 7
## Modify the above example so that if the name is
## "Pluto", it will say "Is it a planet or not?" 


## 7b
## You'll notice that in the "joe" example, the user must
## type "joe" lowercase. Here's how to make it so
## any capitalization works ("Joe", "JOE", etc):
# name = input("What is your name? ")
# print(f"The lowercase version of that is {name.lower()}.")
# if name.lower() == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.")

## 7bb
## Copy and modify the previous example so that
## if the name is "Ruby", it displays
## "That name is also the name of a gem."
## Make it work for any capitalization of Ruby.

## 7c
## Try this. What do you think the != operator means?
# name = input("What is your name? ")
# if name.lower() != "jay": 
#     print("Your name is not Jay.") 
# print("Greetings.")


## 7d
## - Ask the user for a name
## - If the name is anything other than Bob, then
##   display "I don't think I know you. I only know Bob."
## Hint: the != operator means "not equal".


## 7dd
## - Ask the user for a number
## - If the number is not equal to 5, say "You should have picked 5." 
## (Use the != operator)
    

## 7e
## - Ask the user for a name
## - If the name is empty, say "You didn't type anything!"
## - Otherwise, say "Hi ___."
## Hint: an empty name would be quotes with nothing inside, so
##     you might use something similar to this piece of code:
##     if whatTheUserTyped == "":
##           print("Something would go here.")


## 8 
## Try this. 
# age = 10 
# ageNextYear = age + 1 
# print(ageNextYear) 
     

## 9
## Try this. Note: you will get an error. 
# age = input("How old are you?") 
# ageNextYear = age + 1 
# print(ageNextYear) 
     

## 10 
## Try this. 
# age = int(input("How old are you?")) 
# ageNextYear = age + 1 
# print(ageNextYear) 


## 11
## Write a program that satisfies the following examples. Remember that the "✎" indicates user input.
## Example 1:
##   How old are you? ✎ 55
##   I see you are 55 years old.
##   You will be 65 years old in 10 years.
## Example 2:
##   How old are you? ✎ 45
##   I see you are 45 years old.
##   You will be 65 years old in 20 years.

# age = int(input("How old are you?")) 
# agein20yrs = age + 20 
# print(f"You will be {agein20yrs} years old in 20 years.") 

## 12
## Try this. Note: you will get an error. 
# age = int(input("How old are you?"))
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 
     
## 13
## Modify the above example so it works.
## You’ll use the `int` function. 

## 14
## Copy and modify the above example so that
## it shows how many years remain until you can
## drink (but only display that if you’re
## under the drinking age). 

## 15
## Write a program that takes a name from the user.
## If the name is the letter "A", say
## "Your name is just the letter A? That’s kinda cool".
## Otherwise, say "Ok, your name is ___". 

###########################################

## 16
## Try this: 
# birthyear = int(input("Type a year: ")) 
# if birthyear < 2000: 
#     print("You were born before 2000.") 
# elif birthyear == 2000: 
#     print("You were born in 2000.") 
# else: 
#     print("You were born after 2000.") 
  
## 16b
## Try this:
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# elif name == "sue":
#     print("Your name also refers to a legal action.")
# elif name == "rob":
#     print("Another abbreviation for robert, correct?")
# elif name == "lacy":
#     print("Does the origin of your name relate to lace?")
# else:
#     print("I don't know you.")
# print("Done.")
        
## 16c
## Try this. How is it different from the previous example?
## (The difference is subtle, so ask if you are unsure.)
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# if name == "sue":
#     print("Your name also refers to a legal action.")
# if name == "rob":
#     print("Another abbreviation for robert, correct?")
# if name == "lacy":
#     print("Does the origin of your name relate to lace?")
# else:
#     print("I don't know you.")
# print("Done.")

## 17
## Here's an example of using separate if statements,
## that is, a case where you would NOT want to use elif:
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name.startswith("z"):
#     print("Your name starts with a Z. That is somewhat uncommon in English.")
# if len(name) < 3:
#     print("Your name is less than 3 characters long.")
# if len(name) > 9:
#     print("Your name is more than 9 characters long.")
# if name == "":
#     print("Your name is empty!")

## 17b
## Here's another example of the usefulness of elif.
# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# elif heightInInches <= 55:
#     print("That's relatively short.")
# elif heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

## 17c
## Copy and modify the previous example so that each `elif` is
## simply `if`. How does it act differently? 
 
## 18
## Ask the user how many French fries they want.
## Display different responses depending on how many they
## request. (Examples: "That’s way too many!", etc.) 

## 19
## Try this. Did it print what you expected?
# x = int(input("Enter a number: ")) 
# if x < 20: 
#     print("A") 
#     print("B") 
# print("C") 

## 20
## Copy and modify the previous example so
## that C is only printed if the number is not less than 20.
## Use the `else` keyword.

## 20b
## Copy and modify the previous example so that it acts like this:
## if x is less than 20, then print A.
## Otherwise, print C.
## After all of that is done, print Goodbye
## (regardless of what x was.)

## 20c
## Try this.
# x = int(input("Type a number: "))
# if x > 3 and x < 10:
#     print("x is more than 3 and less than 10.")

## 20d
## Here's a shorter way to write the same example:
# x = int(input("Type a number: "))
# if 3 < x < 10:
#     print("x is more than 3 and less than 10.")
    
## 21
## Ask the user for a number.
## If the user gives a number more than 50, 
##    then ask "What is your name?"
##    and display "Hello" followed by the name.
## If the user gives any other number,
##    then ask "How did you pick that number?"
##    and regardless of what they say, display "I see."
## After all of that, say "Have a good day."

## 22
## Write a program that takes a number from the user.
## Display the number doubled.
## Then do a sequence of creative if statements of your choice.
##   For example, if the number is negative,
##   display "Really? Negative? Interesting".

## 22b
## Try this. Why do we use float instead of int here?
# firstcost = float(input("How much is the first thing you bought? "))
# secondcost = float(input("How much is the second thing you bought? "))
# total = firstcost + secondcost
# discounted = total * 0.9
# print(f"""The total cost would be {total}.
# However, we're doing a special sale today, so you get a 10% discount.
# That means you actually pay {discounted}""")

## 23
## Try this.
# x = float(input("Type a non-whole number. "))
# print(f"One more would be {x + 1}.")
## As you can see, you can use `float` instead of
##  `int` when dealing with non-whole numbers.
## Sidenote: 
##   (this sidenote is outside the scope of the class, but good to know)
##   Using floats can cause weird rounding errors. For example:
# print(1.03 - 0.42)
##   This will print 0.6100000000000001.
##   That's quite important when doing comparisons:
# if 0.1 + 0.1 + 0.1 == 0.3:
#     print("This will not print.")
# else:
#     print("This will print... what is math??")
##   The reason is because the numbers are converted to
##   binary behind the scenes,
##   and just as you can't express "one third" exactly in decimal
##   (0.33333 is not EXACTLY one third)
##   you can't express "one tenth" exactly in binary.
##   For more info, see https://docs.python.org/3/tutorial/floatingpoint.html
##   If you plan to eventually do any "real-life" programming,
##   then it's definitely worth reading.
## (end of sidenote)

## 23b
## Ask the user for the cost of a single item
## and the quantity purchased. Print the total cost. 
## Make sure this works for non-integer costs.
## For example, try a cost of 2.30 and quantity of 2.
## Hint: You'll use float instead of int.
## Example:
##   What is the cost for an item? ✎ 2.30
##   How many did you buy? ✎ 2
##   The total cost would be $4.60.

## 24
## Modify the previous example so that the shop gives
## a discount of 10% if you buy at least 20 of an item.  
## For example, if one item costs $5, and you’re buying 20,
## the total cost would be $90. 
     
## 25
## Ask the user for a number
## (make sure to allow for non-whole numbers).
## Print the absolute value of the
## number without using the abs function. 

## 26
## Ask the user for a temperature in Celsius,
## and display the temperature in Fahrenheit. 
## Make sure to allow for non-whole numbers.

## 27
## Same as previous example, but backwards. 

## 28
## Combine the two previous examples: ask the user for
## a number and which way to convert. 

## 29
## Ask the user for a number.
## Using the % operator, display "The remainder of
## your number divided by 5 is ___."
## Also, if the remainder that you calculated is 0,
## display "That number is evenly divisible by 5."

## 30
## Try this.
# color = input("What color is water? ")
# if color == "blue" or color == "transparent":
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

## 31
## Try this.
# color = input("What color is water? ")
# if color in ["blue", "transparent"]:
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

## 32
## Try this.
# color = input("What color is water? ")
# if color != "blue" and color != "transparent":
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

## 33
## Try this.
# color = input("What color is water? ")
# if color not in ["blue", "transparent"]:
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

## 34
## Ask the user what sound a dog makes.
## If the user says any of "woof", "bark", or "ruff",
## then display "That's correct!"
## otherwise, display "Not quite."
## Make it work for any capitalization.

########################################################################
########################################################################

## 1
## Try this. Run it more than once.
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")

## 1b
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.
# import random
# randomnumber = random.randint(1,4)
# print(f"Here's a random integer between 1 and 4: {randomnumber}")

## 1c
## Try this. Run it a few times.
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")

## 1d
## Copy and modify the previous example so that the computer
## will pick numbers between 7 and 10 instead.

## 1e
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"
# import random
# randnumb = random.randint(5, 10)
# print(f"Heres random numbers: {randnumb}")
# if randnumb == 10:
#     print("IIIIIIITTTTTTSSSSSSSSS TTTTTTTTTEEEEEEEEEEEENNNNNNNN")

## 2
## Try this.
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.") 
     
## 3
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.
# import random
# name = random.choice(["John", "Jack", "Jill","Mark"])
# print(f"Hey {name}")
# if name == "Mark":
#     print("Youre the odd one out!")
          
## 3b
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand."
# import random
# name = random.choice(["John", "Jack", "Jill","Mark", "Dell"])
# print(f"Hey {name}")
# if name == "Dell":
#     print("Youre a computer brand!")

## 3c
## Try this.
## Notice that the "Have a good day" line prints regardless of
## the chosen name.  This is because it is
## not indented (it has no spaces before the line).
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Hello Joe!")
#     print("Your name rhymes with low.")
# print("Have a good day.")

##~~~~~~ELSE~~~~~~##

## 4
# import random
# age = random.randint(18,24)
# print(f"If you are {age} years old.")
# if age < 21:
#     print("You are a loser")
# else:
#     print("Get in loser")

# urname = input("What is your name? ")
# if urname == "Santa":
#     print("Saaaaantaaa")
# else:
#     print("Hiiiiiiii")

# name = input("What is your name? ")
# print("Hmmmm interesting! ")
# if name == "Jacob":
#     print(f"{name},Your parents made an awesome choice! ")
# else:
#     print(f"{name}, Your parents chose a horrible name!!")

# name = input("What is your name? ")
# print(f"Hello {name}")
# if name == "Jacob":
#     print("Welcome back, Jacob!! ")
# else:
#     print("I dont know you, I only know Jacob! ")

# name = input("What is your name? ")
# if name == "":
#     print("You didn't type anything!")
# else:
#     print(f"Hi {name}!")

# age = 10
# agenextyear = age +1
# print(agenextyear)

# age = int(input("How old are you? "))
# agenextyear = age + 1
# print(f"Next year you will be, {agenextyear}.")

# age = int(input("How old are you? "))
# print(f"I see you are {age}!!")
# agein10yrs = age + 10
# print(f"You will be {agein10yrs} years old in 10 years.")

# age = int(input("How old are you? "))
# if age < 21:
#     print("You can't drink alocohol in the US yet.")
# else:
#     print("You are legally allowed to drink. Drink Responsibly!")

# age = int(input("How old are you? "))
# sober = 21 - age
# drink = age - 21
# if age < 21:
#     print(f"You can't drink alocohol in the US for another {sober} years.")
# else:
#     print(f"""You are legally allowed to drink for the past {drink} years. 
#           Drink Responsibly!""")
    
# birthyear = int(input("When were you born? "))
# if birthyear < 2000:
#     print("You were born before 2000.")
# elif birthyear == 2000:
#     print("You were born in the year 2000. ")
# else:
#     print("You were born after the year 2000. ")

# name = input("What is your name? ")
# print("Ok, let me look up that name...")

# if name.lower() == "jacob":
#     print("That name used to be common, I think.")
# elif name.lower() == "sue":
#     print("Your name also refers to a legal action.")
# elif name.lower() == "jake":
#     print("Well she sounds hideous!")
# else:
#     print("That's my purse, I don't know you!")

# print("Done!!")

## 17
## Here's an example of using separate if statements,
## that is, a case where you would NOT want to use elif:
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name.startswith("z"):
#     print("Your name starts with a Z. That is somewhat uncommon in English.")
# if len(name) < 3:
#     print("Your name is less than 3 characters long.")
# if len(name) > 9:
#     print("Your name is more than 9 characters long.")
# if name == "":
#     print("Your name is empty!")

###########################################################
###########################################################


