import time
import os
os.system('cls')
countdown = int(input("Please enter the number of seconds: "))

if countdown <= 0:
    print("Please enter a valid number of seconds")
else:
    while True:
        os.system('cls')
        print("|", countdown, "|")
        time.sleep(1)
        os.system('cls')
        countdown-=1
        if countdown == -1:
            break
    print("Bankai!!")