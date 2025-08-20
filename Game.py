import random
from InquirerPy import inquirer
Exit = True
while Exit == True:
    player = inquirer.select(
            message="How many players ???",
            choices= ["Single player", "Two players","Exit"],
        ).execute()
    if player == "Single player":
        computer = random.choice([-1,0,1])
        choice = inquirer.select(
                message="Select your choice",
                choices= ["Rock" , "Paper" , "Scissors"],
            ).execute()
        CompDict = { -1: "Rock" , 0 : "Paper" , 1 : "Scissors"}
        CompChoice = CompDict[computer]
        print(f"Your choice {choice}!")
        print(f"Computer choice {CompChoice}!")
        
        if (CompChoice == choice):
            print("Draw !!!")
        elif(CompChoice!=choice):
            if (computer == -1 and choice == "Scissors" ):
                print("You losee !!!")
            elif(computer == -1 and choice == "Paper"):
                print("You Win !!!")
            elif(computer == 0 and choice == "Scissors"):
                print("You Win !!!")
            elif(computer == 0 and choice == "Rock"):
                print("You losee !!!")
            elif(computer == 1 and choice == "Paper"):
                print("You losee !!!")
            elif(computer == 1 and choice == "Rock"):
                print("You Win !!!")
            else:
                print("something went wrong!! ")
                
    elif (player == "Two players"):
        choice1 = inquirer.select(
                message="Select your choice",
                choices= ["Rock" , "Paper" , "Scissors"],
            ).execute()
        choice2 = inquirer.select(
                message="Select your choice",
                choices= ["Rock" , "Paper" , "Scissors"],
            ).execute()
        print(f"Player 1 : {choice1}!")
        print(f"Player 2 : {choice2}!")

        if (choice2 == choice1):
            print("Draw !!!")
        else:
            if (choice1 == "Rock" and choice2 == "Scissors" ):
                print("Player 1 wins!!!")
            elif(choice1 == "Rock" and choice2 == "Paper"):
                print("Player 2 wins!!!")
            elif(choice1 == "Paper" and choice2 == "Scissors"):
                print("Player 2 wins!!!")
            elif(choice1 == "Paper" and choice2 == "Rock"):
                print("Player 1 wins!!!")
            elif(choice1 == "Scissors" and choice2 == "Paper"):
                print("Player 1 wins!!!")
            elif(choice1 == "Scissros" and choice2 == "Rock"):
                print("Player 2 wins!!!")
            else:
                print("something went wrong!! ")
    else:
        print("Thanks for playing!!")
        break
    