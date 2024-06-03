import os
import random

categories = {"fruits": ["apple", "banana", "orange", "grape", "pear"],
              "animals": ["elephant", "tiger", "zebra", "giraffe", "monkey"],
              "colors": ["red", "blue", "green", "yellow", "orange"]}

def choose_word(category):
    """Choose a random word from the given category."""
    return random.choice(categories[category])

def display_word(word, guessed_letters):
    """Display the word with guessed letters filled in and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(attempts):
    """Display the hangman figure based on the number of attempts left."""
    stages = [
         """
           --------
           |      |
           |      X
           |     /|\ 
           |      |
           |     / \ 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \ 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        """
    ]
    print(stages[attempts])

def get_guess(guessed_letters):
    """Get a valid guess from the user."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess

def hangman():
    """Main function to play the hangman game."""
    global categories
    category = random.choice(list(categories.keys())) 
    word = choose_word(category)
    guessed_letters = []
    attempts = 7
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("\nCategory:", category.capitalize())  
        print("Attempts left:", attempts)
        display_hangman(attempts)
        print("Word:", display_word(word, guessed_letters))
        
        guess = get_guess(guessed_letters)
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
        
        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break
    
    if attempts == 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        display_hangman(attempts)
        print("\nSorry, you've run out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again.lower() in ["yes", "y"]:
        hangman()
    else:
        print("Thanks for playing!")

hangman()
