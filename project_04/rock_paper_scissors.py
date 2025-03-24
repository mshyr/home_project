import random
choose = ["Rock", "Paper", "Scissor"]

computer = random.choice(choose)
user = input("Choose from List ").title()
print("Computer Choose = ", computer)
if user!=choose:
    print("Choose only from list")

    if user==computer:
        print("Match Tie")
    elif user=="Rock" and computer=="Scissor":
        print("You Win")
    elif user == "Paper" and computer == "Rock":
        print("You Win")
    elif user == "Scissor" and computer == "Paper":
        print("You Win")
    else:
        print("You lose")


