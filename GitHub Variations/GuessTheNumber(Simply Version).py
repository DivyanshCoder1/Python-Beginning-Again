import random
from tqdm import tqdm
import time
import os

def gameStart():
    os.system('cls')
    print("Rules:-\n")
    print("1.The number is between 1 to 100(Wait for next version to see number changing !!)\n")
    print("2.You will be given hints as follow ::-- ")
    print(" Too high - +ve difference more than 50")
    print(" Too low - -ve difference more than 50")
    print(" High - +ve diffence between 10 to 49")
    print(" Low - -ve diffence between 10 to 49")
    print(" Slightly high - +ve difference less than 10")
    print(" Slightly low - -ve difference less than 10")
    print("The number of guesses matters here\n")
    print("Preparing a number -- \n")
    for i in tqdm(range(50)):
        time.sleep(0.01)

    realnumb = random.randint(1,100)
    attempt = 0
    def takeUserGuess(attempt):
        userguess = input("\nEnter your guess> ")
        attempt += 1
        checkUserGuess(userguess, attempt)

    def checkUserGuess(userguess, attempt):
        if isinstance(int(userguess), int):
            userguess = int(userguess)
            if userguess == realnumb:
                print("That's it\n")
                print(f"It took you {attempt} guesses!\n")
                time.sleep(3)
                os.system('cls')
                gameStart()
                    
            else:
                if userguess > realnumb:
                    if userguess-realnumb >= 50:
                        print(f"{userguess} is too high")
                    if (userguess-realnumb >=10) and (userguess-realnumb < 50):
                        print(f"{userguess} is high")
                    if (userguess-realnumb >=1) and (userguess-realnumb < 10):
                        print(f"{userguess} is slightly high")
                
                if userguess < realnumb:
                    if abs(userguess-realnumb) >= 50:
                        print(f"{userguess} is too low")
                    if (abs(userguess-realnumb) >=10) and (abs(userguess-realnumb) < 50):
                        print(f"{userguess} is low")
                    if (abs(userguess-realnumb) >=1) and (abs(userguess-realnumb) < 10):
                        print(f"{userguess} is slightly low")
                takeUserGuess(attempt)
        else:
            print("Please enter a valid integer!!")
            takeUserGuess(attempt)
    takeUserGuess(attempt)
gameStart()