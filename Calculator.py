def addition(num1,num2):
    return num1+num2
def Subtraction(num1,num2):
    return num1-num2
def Multiplication(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num1/num2
def Modulas(num1,num2):
    return num1%num2
from InquirerPy import inquirer
Operator = inquirer.select(
        message="=$= Select a Operator =$=",
        choices= ["+","-","/","*","%"],
    ).execute()
num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))

match Operator:
    case "+":
        output= addition(num1,num2)
        print(output)
    case "-":
        output= Subtraction(num1,num2)
        print(output)
    case "*":
        output= Multiplication(num1,num2)
        print(output)
    case "/":
        output= Division(num1,num2)
        print(output)
    case "%":
        output= Modulas(num1,num2)
        print(output)
    case default:
        print("Not valid operator")