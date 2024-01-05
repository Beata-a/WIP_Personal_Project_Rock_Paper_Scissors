# Rock Paper Scissors
# Importing random
import random

# Declaring variables to use them in the while loop. 
# I opted for an input() so that the user can enter their choice accordingly, this will get lower cased to easily compare to the bot choice.
# Declaring a list called choices, the "bot" will then randomly choose one of the elements from that list, as a new variable called random_choice.
# Declaring score variables to keep track of who is the winner.
user_input = input("\n Welcome to Bea's own rock, paper, scissors game! \n  \n Please make your selection to play: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
user_choice = user_input.lower()
choices = ["rock" , "paper" , "scissors"]
random_choice = random.choice(choices)
user_score = 0
bot_score = 0

# While loop where the exiting clause is the word exit. So this will keep looting until the word exit is entered.
while user_choice != "exit":
     
#If user choice is not one of the three elements in the list, it will prompt the user to enter their choice again.
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        user_score += 0
        bot_score += 0
        user_input = input("\n  \nThat is not a valid option. \n \n Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
        user_choice = user_input.lower()
        choices = ["rock" , "paper" , "scissors"]
        random_choice = random.choice(choices) 

# Else if the element that the user chose is the same as the one that the bot has chosen, no points awarded, the following is displayed.  
    elif user_choice == random_choice:
        user_score += 0
        bot_score += 0
        print("\n  \nThe computer also selected " , user_choice , ". Are you a computer?")
        user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n" )
        user_choice = user_input.lower()
        choices = ["rock" , "paper" , "scissors"]
        random_choice = random.choice(choices)

# Paper beats rock. Adds a point for the user.
    elif user_choice == "paper" and random_choice == "rock":
        user_score += 1
        print("\n  \nPaper beats rock! That's a point for you buddy.")
        user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
        user_choice = user_input.lower()
        choices = ["rock" , "paper" , "scissors"]
        random_choice = random.choice(choices)

# Rock beats scissors. Adds a point for the user.
    elif user_choice == "rock" and random_choice == "scissors":
        user_score += 1
        print("\n  \nRock beats scissors! That's a point for you buddy.")
        user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
        user_choice = user_input.lower()
        choices = ["rock" , "paper" , "scissors"]
        random_choice = random.choice(choices)
    
# Scissors beat paper. Adds a point for the user.
    elif user_choice == "scissors" and random_choice == "paper":
         user_score += 1
         print("\n  \nScissors beat paper! That's a point for you buddy.")
         user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
         user_choice = user_input.lower()
         choices = ["rock" , "paper" , "scissors"]
         random_choice = random.choice(choices)

# Rock beats scissors. Adds a point to the bot.
    elif user_choice == "scissors" and random_choice == "rock":
         bot_score += 1
         print("\n  \nRock beats scissors!! Better luck next time amigo!")
         user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
         user_choice = user_input.lower()
         choices = ["rock" , "paper" , "scissors"]
         random_choice = random.choice(choices)

# Scissors beat paper. Adds a point to the bot.
    elif user_choice == "paper" and random_choice == "scissors":
         bot_score += 1
         print("\n  \nScissors beat paper!! Better luck next time amigo!")
         user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
         user_choice = user_input.lower()
         choices = ["rock" , "paper" , "scissors"]
         random_choice = random.choice(choices)

# Paper beats rock. Adds a point to the bot.
    elif user_choice == "rock" and random_choice == "paper":
         bot_score += 1
         print("\n  \nPaper beats rock!! Better luck next time amigo!")
         user_input = input("Please make your selection to continue: \n ENTER EXIT TO LEAVE THE SIMULATION \n  \n")
         user_choice = user_input.lower()
         choices = ["rock" , "paper" , "scissors"]
         random_choice = random.choice(choices)

# The first if will have to have another thing that would determine if someone never played a game and exited as soon as they ran the code. MAybe a counter.
if user_choice == "exit" and user_score == 0 and bot_score == 0:
    print("\n  \nSORRY THAT YOU DIDN'T WANT TO PLAY WITH THE BOT. \n EXITING THE SIMULATION. \n  PLEASE HAVE A GOOD DAY.")

elif user_choice == "exit" and user_score == bot_score:
    print("\n  \nYOU DREW WITH A MACHINE. WHAT A SHAME.. \n  \n EXITING THE SIMULATION. \n  PLEASE HAVE A GOOD DAY.")
            
elif user_choice == "exit" and user_score > bot_score:
    print("\n  \nCONGRATULATIONS! THE SCORE IS" , user_score , "TO" , bot_score, ". YOU HAVE BEAT THE BOT.\n HOPE YOU HAD A BLAST. o/ \n  \n EXITING THE SIMULATION. \n  PLEASE HAVE A GOOD DAY.")

    
elif user_choice == "exit" and user_score < bot_score:
     print("\n  \nTHE BOT HAS WON!. THE SCORE IS" , user_score , "TO" , bot_score, ". BETTER LUCK NEXT TIME LOSER! o/ \n  \n EXITING THE SIMULATION. \n  PLEASE HAVE A GOOD DAY.")


