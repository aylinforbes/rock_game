import random
print("-----------------------------")
print("   Rock Paper Scissors")
print("-----------------------------")

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = str(random.choice(possible_actions))
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print("Game Tied")
    elif user_action == "rock":
        if computer_action == "paper":
            print("You lose!")
        else:
            print("You win.")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("You lose")
        else:
            print("You win.")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("You lose!")
        else:
            print("You win")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing")
        break