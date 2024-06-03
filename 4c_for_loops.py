## 1
## Try this:
# colors = ["red", "orange", "yellow"]
# for color in colors:
#     print("Here is a color that I know:")
#     print(color)
#     print()
# print("-----------------------")
# print("The for-loop has ended.")

## 2
## This is a way to imagine how the code above works.
# colors = ["red", "orange", "yellow"]

# color = colors[0]
# print("Here is a color that I know:")
# print(color)
# print()

# color = colors[1]
# print("Here is a color that I know:")
# print(color)
# print()

# color = colors[2]
# print("Here is a color that I know:")
# print(color)
# print()

# print("-----------------------")
# print("The for-loop has ended.")

## 3
## Try this:
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Hello {name}.")
# print("Welcome to the Python course.")

## 4
## Copy and modify the previous example like so:
## for each name, display "Have a good day, ____. I hope you enjoyed 
## experimenting with python."
## (Fill in the blank with the name.)

## 5
## Try this:
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print()

## 6
## Copy and modify the previous example so that for each age,
## it displays "5 years ago, that person was ___ years old."

## 7
## For each of the following numbers, display 
## "Half of __ is ___". For example, "Half of 21 is 10.5"
# numbers = [21, 40, 32, 10, 8, 3]

## 8
## Try this:
# for num in range(1,5):
#     print(num)

## 9
## Copy and modify the previous example to print the numbers 1 to 6.

## 10
## Try this.
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")

## 11
## Try this.
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 90:
#         print("That's hot.")

## 12
## Copy and modify the previous question to display 
## the temperature and display whether it is above or below freezing.

## 12b
## Try this to see the impact of indentation. How do you fix it?
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print("Looking at the temperatures.")
# print(f"One of the temperatures in the list is {temp}")
# if temp > 90:
#     print("That's hot.")

## 13
## Try this:
# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# print("That's all I have to say.")

## 14
## Modify the previous example so that if the user input ends with "day",
## then the computer will display "I think that's a day of the week."

## 15
## Try this:******************************************************************
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# berryCount = 0
# for fr in fruits:
#     if fr.endswith("berry"):
#         berryCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {berryCount} that ended with berry.")

## 16
## Using `startswith` (which works quite similarly to endswith),
## count how many of the fruits start with 'm'.
## Then display the count.

## 17
## Given this list, count how many temperatures are above freezing.
## Display the count.
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]

## 18
## Copy and modify the previous example to show the user how many
## temperatures are above freezing and how many are below freezing.

## ## For loops and files
## Automating processes is one of the many useful applications of computers. 
## In the examples below, we will read the lines of a text file and iterate 
## over the lines using a for loop.

## 19
## Before running this exercise, create a text file called "words.txt" 
## with three lines of text in it.
## Then, try this.
# f = open("words.txt", "r", encoding="utf-8")
# lines = f.read().splitlines()
# f.close()
# print(f"Loaded {len(lines)} lines:")
# print(lines)

## 20
## Try this.
# f = open("words.txt", "r", encoding="utf-8")
# lines = f.read().splitlines()
# f.close()
# for line in lines:
#     print(f"From the file: {line}")

# Bob:red
# Lacy:blue
# Sue:green

## 21
## Try this.
# f = open("names_and_colors.txt", "r", encoding="utf-8")
# lines = f.read().splitlines()
# f.close()
# for line in lines:
#     na, co = line.split(":")
#     print(f"First: {na}. Second: {co}")

## 22
## Copy and modify the previous example.
## Make it so it shows the following output:
##   Bob's favorite color is red.
##   Lacy's favorite color is blue.
##   Sue's favorite color is green.
## Note: Your Python code should mention neither names (Bob, etc) 
## nor colors (red, etc).

## 23
## Given a file with these contents:
##   Bob:red
##   Lacy:blue
##   Sue:green
##   Joe:blue
##   Frank:red
## Display which people like blue.
## Example run:
##    These people like blue:
##    Lacy
##    Joe
## As before, the names and colors should not appear in your Python code.

## 24
## Copy and modify the previous example to allow 
## the user to pick the color of interest.
## Example run 1:
##   Filter by color:  red
##   Bob
##   Frank
## Example run 2:
##   Filter by color:  green
##   Sue

## 25
## Copy and modify the previous example to
## count how many people matched the specified color.
## Example run 1:
##   Filter by color:  red
##   Bob
##   Frank
##   Found 2 match(es).
## Example run 2:
##   Filter by color:  green
##   Sue
##   Found 1 match(es).

## 26
## Copy and modify the previous example to
## count how many people matched the specified color.
## Example run 1:
##   Filter by color:  red
##   Bob
##   Frank
##   Found 2 match(es).
## Example run 2:
##   Filter by color:  green
##   Sue
##   Found 1 match(es).

## 26b
## Given a file with these contents:
##   Bob:red:70
##   Lacy:blue:65
##   Sue:green:72
##   Joe:blue:68
##   Frank:red:71
## Assuming the third column is the heart rate, display the names of people
## whose heart rate is less than 70.
## Example run:
##    These people like have a heart rate that is less than 70:
##    Lacy
##    Joe
## As before, the names and heart rates should not appear in your Python code.

