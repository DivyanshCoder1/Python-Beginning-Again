import os
import time
from questiondata import q_list, option_list, correct_answer_index, money_sum_list

print("Welcome to KBC")
userAction = input("Press enter to start the game!!!")
os.system('cls')

def gamestart():
    '''This function is sort of in a loop, you need to closed the terminal to close the program'''
    os.system('cls')
    money_won = 0
    while True:
        os.system('cls')
        for i in range(0,10):
            print(q_list[i])
            for j in range(0,4):
                print(option_list[i][j])
            print()
            try:
                userInput = int(input("Please enter the correct option number{1,2,3,4}: "))
                if 1<= userInput <=4:
                    if userInput == correct_answer_index[i]+1:
                        print("Correct Answer!")
                        money_won = money_sum_list[i]
                        os.system('cls')
                        print(f"Current Money: {money_won} ruppees")
                        continue
                    else:
                        print("Wrong Answer, you lose!!")
                        break
                else:
                    print("Please enter valid answer, The game will restart in 3 seconds")
                    time.sleep(3)
                    gamestart()
            except:
                print("Please enter valid answer, The game will restart in 3 seconds")
                time.sleep(3)
                gamestart()

        break
    os.system('cls')
    print("Game Over!!!")
    print(f"You won {money_won} ruppees")
    userAction2 = input("Press enter to play again")
    gamestart()

gamestart()
