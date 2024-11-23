# rock paper scissor !
# rock paper - paper
# paper scissor - scissor
# rock scissor -rock
from random import randint
List = ["Rock","Paper","Scissor"]
computer = List[randint(0,2)]
player = False

while player == False:
    player = input("Rock , Paper or Scissor\n")
    if computer == player:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer} beats Rock")
        else:
            print(f"You win! Rock beats {computer}")
    elif player == "Paper":
        if computer == "Rock":
            print(f"You win ! Paper covers {computer} ")
        else:
            print(f"You lose ! {computer} cuts paper ")
    elif player == "Scissor":
        if computer == "Paper":
            print(f"You win Scissor cuts {computer} ")
        else:
            print(f"You lose !{computer} breaks scissor")
    else:
        print("Invalid Input")
    
    play_again = input("Do you want to play again? y/n\n")
    if play_again == "y":
     player = False
     computer = List[randint(0,2)]
    else:
        player = True
# scissor , paper - you win
# scissor , rock - you lose






    




