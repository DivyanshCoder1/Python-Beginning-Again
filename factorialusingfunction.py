def upperfunc():
    def calcfact(num):
        if num == 1 or num==0:
            return 1
        else:
            fact = num * calcfact(num-1)
            return fact
    userInput = input("Please enter the number: ")
    if int(userInput) < 0:
        print("Invalid Value")
        upperfunc()
    elif userInput == "exit":
        exit()
    else:
        print(calcfact(int(userInput)))
        upperfunc()
upperfunc()