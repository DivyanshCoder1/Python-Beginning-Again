import random

wordlist = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

myword = wordlist.split()[random.randint(0,16)]
mywordlist = list(myword)
print(myword)
attempts =len(myword) + 10
guessedchar = {}
guesslist = []

def congrats():
    print()
    print("You win!")

while True:
    print()
    print(f"Guess the character:(You have {attempts} attempts left)", end=": ")
    userGuess = input("")
    if userGuess in myword:
        index = myword.index(userGuess)
        guessedchar[f"{index}"] = userGuess
        guesslist.append(userGuess)
        for i in range(len(myword)):
            if str(i) in guessedchar:
                print(guessedchar[str(i)], end=" ")
                continue
            print("_", end=" ")
        if sorted(list(myword)) == sorted(guesslist):
            congrats()
    else:
        print("Not in the word")
    
    attempts -= 1

    if attempts == 0:
        print("All attempts have been fnished")
        break
    


