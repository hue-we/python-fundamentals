import random

def roll_dice():
    return random.randint(1,6)

print("Welcome to the Dice Roller!")
while True:
    input("Press Enter to roll....")
    result = roll_dice()
    print(f"You rolled a {result}!")

    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break
    