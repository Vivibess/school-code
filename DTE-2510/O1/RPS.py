import random

def rps_game(pc_choice, user_choice):
        if pc_choice == rps[user_choice]:
            return "Draw"
        elif pc_choice == rps[user_choice-1]:
            return "You win"
        elif pc_choice == rps[user_choice-2]:
            return "You lose"

rps = [0, 1, 2]
pc_choice = random.choice(rps)

while True:
    try:
        user_choice = int(input("Please choose rock, paper, or scissors as 0, 1, or 2\n"))
        if user_choice in rps:
            break
        elif user_choice == "exit":
            quit()
        else:
            print("That's not a valid input, please try again.")
    except ValueError:
        print("That's not a valid input, please try again.")

print("The PC chose", ["rock", "paper", "scissors"][pc_choice], ", and you chose", ["rock", "paper", "scissors"][user_choice])
print(rps_game(pc_choice, user_choice))