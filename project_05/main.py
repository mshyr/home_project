import random

# List of words to choose from
words = ["apple", "banana", "grape"]

# Pick a random word from the list
word = random.choice(words)

# Make a list of underscores for hidden letters
hidden_word = ["_"] * len(word)

# Number of tries the player gets
tries = 6

print("Welcome to Hangman!")

# Main game loop
while tries > 0:
    # Show the current state of the word
    print(" ".join(hidden_word))
    
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is in the word
    if guess in word:
        # Reveal the guessed letter in the hidden word
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("Good job!")
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)
    
    # Check if the player guessed all letters
    if "_" not in hidden_word:
        print("You win! The word was:", word)
        break

# If player runs out of tries
if tries == 0:
    print("Game over! The word was:", word)
