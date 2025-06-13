import math
import os
os.system('cls')
gamedict = {"row1":["1", "2", "3"],
            "row2":["4", "5", "6"], 
            "row3":["7", "8", "9"]}
                
def takeX():
    print()
    userInput = int(input("Please enter the numeber for X: "))
    makeX(userInput)

def takeO():
    print()
    userInput = int(input("Please enter the numeber for O: "))
    makeO(userInput)

def makeX(userInput):
    os.system('cls')
    if 1<= userInput <=3:
        gamedict["row1"][userInput-1] = "X"
        printer()
    if 4<= userInput <=6:
        gamedict["row2"][userInput-4] = "X"
        printer()
    if 7<= userInput <=9:
        gamedict["row3"][userInput-7] = "X"
        printer()
    takeO()

def makeO(userInput):
    os.system('cls')
    if 1<= userInput <=3:
        gamedict["row1"][userInput-1] = "O"
        printer()
    if 4<= userInput <=6:
        gamedict["row2"][userInput-4] = "O"
        printer()
    if 7<= userInput <=9:
        gamedict["row3"][userInput-7] = "O"
        printer()
    takeX()

def printer():
    os.system('cls')
    for i in range(1,4):
        print()
        rowlist = gamedict[f"row{i}"]
        for j in range(0,3):
            print(rowlist[j], end = " ")

printer()
takeX()