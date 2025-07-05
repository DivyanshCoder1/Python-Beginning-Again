user_input = input("Enter the comment: ")

spam_list = ["make a lot of money", "buy now", "subscribe this", "click this"]

def spamfounder(userinput):
    for spam_word in spam_list:
        if spam_word in user_input.lower():
            return "This is spam"
    return "This is not spam"

print(spamfounder(user_input))
        