import random

# 👉 Possibilities 🎱!
random_replies = [
    "It is Certain", 
    "Yes", 
    "You may rely on it", 
    "Ask again later",
    "You've Got to be Kidding",
    "Reply hazy, try again",
    "My reply is NO WAY",
    "My sources say no" 
    ]

# 👉 Directions to Possibilities 🎱!
while True:
    user_input = input("Ask the 🎱 a question, or enter 'no' to quit: ").lower()
    
    if user_input.lower() in ["no", "n"]:
        print("Goodbye, See you next time. ")
        break

    else:
        print(random.choice(random_replies))
