import os
import random
import time
os.system("cls")
def rolldice():
    for i in range(1, 15):
        print("|", random.randint(1,6), "|")
        time.sleep(0.1)
        os.system("cls")
    print("|", random.randint(1,6), "|")
    userInput  = input("Press enter to roll again: ")
    rolldice()
rolldice()