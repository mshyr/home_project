import random

print("Think Your Number Between 1 and 20...")
# variable declaring and assign value 
low = 1
high = 20

while True:
    guess = random.randint(low, high)
    print(f"Computer Guessed a Number {guess}... \nIs This Your Number?")
    reply = input("Enter (C) if Number is Correct, Enter (H) if Number is High and (L) If Number is Low : ").lower()
    
    if reply == 'c':
        print(f"Computer Guessed Your Number.\nYour Number was {guess}")
        break
    elif reply == 'h':
        high = guess - 1
    elif reply == 'l':
        low = guess + 1
    else:
        print("Please Enter only H, L, or C.")
