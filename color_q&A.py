######################################################
print("Hello!")
color = input("What is your favorite color? ")
print(f"{color} is a pretty color")
while True:
    user_input = input("Do you have another color you like? (yes/no): ")
    if user_input.lower() in ["yes", "y"]:
        color2 = input("What is your next favorite color? ")
        print(f"{color2}, That's a horrible color!")
        break
    elif user_input.lower() in ["no", "n"]:
        print("You suck at life")
        break
    else:
        print("Invalid input. Please enter yes/no.")
        continue
#######################################################