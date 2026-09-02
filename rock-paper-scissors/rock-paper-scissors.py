import random

options = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors")
print("First to 3 wins takes it.\n")

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in options:
        print("That's not a valid choice, try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print(f"Score: You {player_score} - {computer_score} Computer\n")

if player_score == 3:
    print("You won the match!")
else:
    print("Computer won the match!")