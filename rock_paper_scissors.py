# Rock, Paper, Scissors Game
import random

choices =["Rock", "Paper", "Scissors"] 
computer = random.choice(choices)
playing = True

comp_score = 0
player_score = 0


# Print opening statement
print('WELCOME TO ROCK, PAPER, SCISSORS!!')

while playing:    
    
    player = input('Make your move. Type Rock, Paper or Scissors: ').capitalize()

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer =="Paper":
            print("You lose!", computer, "covers", player)
            comp_score +=1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer =="Scissors":
            print("You lose!", computer, "cut", player)
            comp_score +=1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer =="Rock":
            print("You lose!", computer, "smashes", player)
            comp_score +=1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    else:
        print("Input not recognized. Try again. Please type Rock, Paper or Scissors")
        continue

    replay = input("Do you want to play again? Type Yes or No: ").capitalize()

    if replay == "Yes":
        playing = True
        continue
    elif replay == "No":
        print ('Thank you for playing!')
        print("Player scored:", player_score,", Computer scored:", comp_score )
        break
    else:
        print("I don't understand. Please type Yes or No")

    
    
        

         




    