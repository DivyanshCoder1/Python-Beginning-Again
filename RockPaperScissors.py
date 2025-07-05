import random
import time
import os

def overallfunc():
    computer_points = 0
    user_points = 0
    os.system('cls')
    choices = "RPS"
    computer_choice = random.choice(choices)
    conditions = ["RR", "RP", "RS",
                "PR", "PP", "PS",
                "SR", "SP", "SS"]
    outcome_condition = ["D", "H", "C",
                        "C", "D", "H",
                        "H", "C", "D"]
    def gameOver(winner):
        if winner == "quit":
            print("Game Over!!!")
            userInput = input("Press enter to restart")
            os.system('cls')
            take_user_choice(0,0)
        else:
            print(f"{winner} scored 5 points.{winner} won")
            time.sleep(3)
            overallfunc()

    def compare(user_choice, computer_choice, computer_points, user_points):  
            list_item = computer_choice + user_choice
            index = conditions.index(list_item)
            if outcome_condition[index] == "D":
                print("Draw!")
                print()
                take_user_choice(computer_points, user_points)
            elif outcome_condition[index] == "H":
                print("You Win!")
                print()
                user_points += 1
                take_user_choice(computer_points, user_points)
            elif outcome_condition[index] == "C":
                print("Computer Wins!")
                print()
                computer_points +=1
                take_user_choice(computer_points, user_points)
        
    def choice_animation(user_choice):
        for i in range(10):
            time.sleep((i+1)*0.001)
            os.system('cls')
            print("|", user_choice,"| v/s |" ,random.choice(choices), "|")
        os.system('cls')
        print("|", user_choice,"| v/s |" ,computer_choice, "|")
        return computer_choice

    def take_user_choice(computer_points, user_points):
        choices = "RPS"
        global computer_choice
        computer_choice = random.choice(choices)
        print("Current Score: ")
        print("Computer's Score: ", computer_points)
        print("Your Score: ", user_points)
        if computer_points == 5:
            gameOver("Computer")
        elif user_points == 5:
            gameOver("You")
        else:
            print()
            print("You can press q to exit")
            user_choice = str(input("Enter your choice: (R/P/S)   ")).upper()
            if user_choice == "Q":
                gameOver("quit")
            elif user_choice != "R" or "P" or "S":
                print("Invalid Choice!!")
                print("The game will restart in 3 seconds")
                time.sleep(3)
                take_user_choice(computer_points, user_points)
            else:
                os.system('cls')
                print("Computer's choice is ", choice_animation(user_choice))
                print("Your choice is: ", user_choice)
                print()
                compare(user_choice, computer_choice, computer_points, user_points)

    take_user_choice(computer_points, user_points)
overallfunc()