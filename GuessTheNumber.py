import random

Computer = random.randrange(1,50)
option = []
chances = 0
while len(option)!=5:
    randomOption = random.randrange(Computer-3,Computer+3)
    if randomOption not in option:
        option.append(randomOption)

hints = [num for num in option if 1 <= num <= 50]
while chances <3:
    User = int(input("Enter your Guessed Number between 1-50 : "))
    if (User <=50 and User >=1):
        if Computer == User:
            print("You won !!!")
            break
        else:
            chances +=1
            if chances <=2:
                print(f"The Number is among this hints : {hints}")
            else:
                print("Better luck next time!!")
    else:
        print("Number is out of range.")
        break