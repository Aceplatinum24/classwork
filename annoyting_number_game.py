##ANNOYING NUMBER GAME##

#time data
# import time
# def delay_print(s):
#     for c in s:
#         print(c, end="", flush=True)
#         time.sleep(0.03)


# number = ""
# while True:
#     number = input("Please select any number! ")
#     user_input = input("Are you sure about that number? (yes/no): ")

# #Yes data    
#     if user_input.lower() in ["yes", "y"]:
#         number2 = input("Type your number again to confirm... ")  
#         if number == number2:
#             delay_print(f"Thank you for confirming the number, {number2}.\n")
#         if number != number2:
#             delay_print("Why you always lying? \n")
#         break

# #No Data
    # elif user_input.lower() in ["no", "n"]:
    #     number3 = input("What would you like your new number to be? ")
    #     number3confirm = input("Can you confirm what your new number will be? ")
    #     if number3 == number3confirm:
    #         delay_print(f"Thank you for confirming, {number3}\n")
    #     if number3 != number3confirm:
    #         delay_print(f"The number you have input does not match the previous number you entered, Try Again!! \n")
    #         continue

# #Invalid response
#     else:
#         print("Invalid input. Please enter yes/no.")
