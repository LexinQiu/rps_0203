


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# process user inputs
print("Rock, Paper, Scissors, Shoot!")

u = input("Please choose one of: 'rock', 'paper', 'scissors': ")
print("User chose:", u)



# validate user inputs







# simulate computer selection

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:", computer_choice)


# determine the winner

if u == computer_choice:
    print("It's a tie!")
elif u == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif u == "rock" and computer_choice == "scissors":
    print("You win!")
elif u == "scissors" and computer_choice == "rock":
    print("Computer wins!")
elif u == "scissors" and computer_choice == "paper":
    print("You win!")
elif u == "paper" and computer_choice == "scissors":
    print("Computer wins!")
else:    
    print("Computer wins!")


# display final results



