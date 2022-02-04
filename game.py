


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# process user inputs

print("Welcome 'Player One' to my Rock-Paper-Scissors game.")

u = input("Please choose one of: 'rock', 'paper', 'scissors': ")
print("User chose:", u)



# validate user inputs

v = u.lower()
if v in ['rock','paper','scissors']:
    print("Good choice!")
else:
    print("You entered an invalid option. The game stopped.")
    quit()




# simulate computer selection

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:", computer_choice)


# determine the winner

if u == computer_choice:
    print("It's a tie!")
elif u == "rock" and computer_choice == "paper":
    print("Oh, the computer won. It's ok.")
elif u == "rock" and computer_choice == "scissors":
    print("Congratulations! You won!")
elif u == "scissors" and computer_choice == "rock":
    print("Oh, the computer won. It's ok.")
elif u == "scissors" and computer_choice == "paper":
    print("Congratulations! You won!")
elif u == "paper" and computer_choice == "scissors":
    print("Oh, the computer won. It's ok.")
else:    
    print("Oh, the computer won. It's ok.")


# display final results
print ("Thanks for playing. Please play again!")

#player name customization
import os

player_name = os.getenv("PLAYER_NAME", default="Player One")
