import random

def congrats(attempts, myword):
    print()
    print(f"You win! The word is: {myword.upper()}")
    print(f"You guessed it with {attempts} attempts!!")
    startgame()

def startgame():
    wordlist = '''apple banana mango strawberry 
    orange grape pineapple apricot lemon coconut watermelon 
    cherry papaya berry peach lychee muskmelon'''

    myword = wordlist.split()[random.randint(0,len(wordlist.split()) - 1)]
    # myword = "muskmelon"
    mywordlist = list(myword)
    totalattempts =len(myword) + 10
    attempts = 0
    guesslist = []
    emptylist = ["_"] * len(myword)
    print("--------------------------------------------------------")
    while True:
        print(f"Guess the character:(You have {totalattempts} attempts left)", end=": ")
        userGuess = input("")
        if userGuess.lower() in mywordlist:
            index = mywordlist.index(userGuess.lower())
            mywordlist[index] = "_"
            emptylist[index] = userGuess.lower()
            guesslist.append(userGuess.lower())
            print(" ".join(emptylist))
            if sorted(list(myword)) == sorted(guesslist):
                congrats(attempts,myword)
                break
        elif userGuess.lower() == "exit":
            exit()
        else:
            print("Not in the word")
        
        attempts += 1
        totalattempts -=1

        if totalattempts == 0:
            print("All attempts have been finished")
            print(f"The word was {myword}")
            startgame()
            break
    
startgame()