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

num1=int(input("Enter the number 1 : "))
Operator = str(input("Enter the Operator : "))
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