print("This is a simple calculator")
print()
num1 = 0
num2 = 0

def checkforanotheroperator():
    print()
    print("Do you wish to use the same numbers for different operations or wish to change the numbers(Enter operator of new operator with same number or press enter for new numbers)")
    userinput = input("> ")
    print()

    if userinput == "":
        takeinput()

    else:
        calc(num1,num2,userinput)

def calc(num1,num2,operator):
    if num1 or num2 or operator == "" or " ":
        print("\nPlease enter valid values\n")
        takeinput()
    
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        print(num1 + num2)

    if operator == "-":
        print(num1 - num2)

    if operator == "*":
        print(num1*num2)

    if operator == "/":
        if num1>num2:
            print(num1/num2)
        else:
            print(num2/num1)

    if operator == "//":
        if num1>num2:
            print(num1//num2)
        else:
            print(num2//num1)

    if operator == "**":
        print(num1**num2)

    if operator == "%":
        print(num1%num2)
    checkforanotheroperator()

def takeinput():
    print("Enter first number")
    global num1
    num1 = input("> ")
    print()
    print("Enter second number")
    global num2
    num2 = input("> ")
    print()
    print("Enter the operator[+,-,*,/,//,%,**]")
    operator = input("> ")
    calc(num1,num2,operator)

takeinput()