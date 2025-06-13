import random
from tqdm import tqdm
import time
import os
os.system('cls')
def gameStart():
    os.system('cls')
    print("Rules:-\n")
    print("1.The range of the number will be asked, do not forget that the larger range you choose, the more harder the game becomes\n")
    print("2.You will be given hints after deciding what is extremely high-low, too high-low, high-low, slightly high-low after the system determines these values by capturing your max number")
    print("The number of guesses matters here\n")
    
    def takemaxnumber():
        print("\nPlease enter the max number you want(The random number will be choosen from 1 to the number you choose!!)")
        maxnumber = int(input("> "))

        if maxnumber > 500:
            print("The max limit is 500, enter a number less than that!!")
            takemaxnumber()
        return maxnumber
    maxnumber = takemaxnumber()
    extremelyrange = maxnumber//2
    toorange = maxnumber//4
    normalrange = maxnumber//8
    slightlyrange = maxnumber//16
    rangestring = f"""
    Extreme is greater {extremelyrange}
    Too is {toorange} to {extremelyrange}
    Normal is {normalrange} to {toorange}
    Slightly is {slightlyrange} to {normalrange}
    Very close is upto 1 to {slightlyrange}
    """
    print(rangestring)
    print("Preparing a number -- \n")
    for i in tqdm(range(50)):
        time.sleep(0.01)
    realnumb = random.randint(1,maxnumber)
    print(f"The real number is {realnumb}")
    attempt = 0
    def takeUserGuess(attempt):
        userguess = int(input("\nEnter your guess> "))
        attempt += 1
        checkUserGuess(userguess, attempt)

    def checkUserGuess(userguess, attempt):
        if isinstance(userguess, int):
            userguess = int(userguess)
            if userguess == realnumb:
                print(f"That's it\nThe number is {realnumb}")
                print(f"It took you {attempt} guesses!\n")
                print("Game will restart is 5 seconds")
                time.sleep(5)
                os.system('cls')
                gameStart()
                    
            else:
                if userguess>maxnumber:
                    print("This number is out of selected range!!")
                    takeUserGuess(attempt)
                else:
                    extremelyrange = maxnumber//2
                    toorange = maxnumber//4
                    normalrange = maxnumber//8
                    slightlyrange = maxnumber//16

                    if userguess > realnumb:
                        if userguess-realnumb >= extremelyrange:
                            print(f"{userguess} is extremely high")
                        if (userguess-realnumb >=toorange) and (userguess-realnumb < extremelyrange):
                            print(f"{userguess} is too high")
                        if (userguess-realnumb >=normalrange) and (userguess-realnumb < toorange):
                            print(f"{userguess} is high")
                        if (userguess-realnumb >= slightlyrange) and (userguess-realnumb < normalrange):
                            print(f"{userguess} is slightly high")
                        if ((userguess-realnumb) >= 1) and (userguess-realnumb < slightlyrange):
                            print(f"{userguess} is very close")
                    
                    if userguess < realnumb:
                        if abs(userguess-realnumb) >= extremelyrange:
                            print(f"{userguess} is extremely low")
                        if (abs(userguess-realnumb) >= toorange) and (abs(userguess-realnumb) < extremelyrange):
                            print(f"{userguess} is too low")
                        if (abs(userguess-realnumb) >= normalrange) and (abs(userguess-realnumb) < toorange):
                            print(f"{userguess} is low")
                        if (abs(userguess-realnumb) >= slightlyrange) and (abs(userguess-realnumb) < normalrange):
                            print(f"{userguess} is slightly low")
                        if (abs(userguess-realnumb) >= 1) and (abs(userguess-realnumb) < slightlyrange):
                            print(f"{userguess} is very close")
                    takeUserGuess(attempt)
        else:
            print("Please enter a valid integer!!")
            takeUserGuess(attempt)
    takeUserGuess(attempt)
gameStart()