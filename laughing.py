import os
import time

# Define the frames for the laughing face
frame1 = """
      __________                __________
     |          |              |          |
      \   -    /                \    -   /
       ````````                  ````````
                        `
                         `
                          `
                        `
                _________________
           
          """

frame2 = """
      __________                __________
     |          |              |          |
      \   o    /                \    o   /              
       ````````                  ````````              
                        `                              
                         `                         
                          `
                        `
            _________________________
           |                         |
           |                         |
            \                       /
             ```````````````````````



          """

frame3 = """
      __________                __________
     |          |              |          |
      \   ()   /                \    ()  /              
       ````````                  ````````              
                        `                              
                         `                          
                          `
                        `
            _________________________
           |                         |
           |                         |
           |                         |
            \                       /
             ```````````````````````







"""
    
#     _______________
#    (               )
#    ( L O S E R ! ! )
# <==(_______________) 


# Define the number of repetitions
repetitions = 100000

# Loop for the specified number of repetitions
for _ in range(repetitions):
    # Display each frame with a delay
    for frame in [frame1, frame2, frame3, frame2]:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the frame
        print(frame)
        # Add a delay
        time.sleep(0.08)  # Adjust the delay as needed

# import time

# def print_chat_bubble(message):
#     # Define the size of the chat bubble
#     width = len(message) + 4
#     height = 3
    
#     # Print the top of the chat bubble
#     print("╔" + "═" * (width - 2) + "╗")
    
#     # Print the message with padding
#     print("║ " + message + " ║")
    
#     # Print the bottom of the chat bubble
#     print("╚" + "═" * (width - 2) + "╝")

# # Get user input
# message = input("Enter your message: ")

# # Print the chat bubble
# print_chat_bubble(message)

# # Simulate typing effect
# for char in message:
#     time.sleep(0.1)
#     print("\b \b" + char, end="", flush=True)  # Backspace to erase the character

# print()  # Move to the next line
