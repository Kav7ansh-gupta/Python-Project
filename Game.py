import random

computer = random.choice([-1,0,1])
You = input("Enter r for Rock , p for paper , s for scissors: ")
YourDict= {"r": -1,"p": 0,"s": 1}
CompDict = { -1: "Rock" , 0 : "Paper" , 1 : "Scissors"}
YourChoice = YourDict[You]

print(f"Your choice {CompDict[YourChoice]}!")
print(f"Computer choice {CompDict[computer]}!")

if (computer == YourChoice):
    print("Draw !!!")
else:
    if (computer == -1 and YourChoice == 1 ):
        print("You losee !!!")
    elif(computer == -1 and YourChoice == 0):
        print("You Win !!!")
    elif(computer == 0 and YourChoice == 1):
        print("You Win !!!")
    elif(computer == 0 and YourChoice == -1):
        print("You losee !!!")
    elif(computer == 1 and YourChoice == 0):
        print("You losee !!!")
    elif(computer == 1 and YourChoice == -1):
        print("You Win !!!")
    else:
        print("Some thing went wrong.")