list_word = ["hello", "world"]

word = input("Enter the word to remove: ")

def removeword(word):
    if word.lower() in list_word:
        list_word.remove(word.lower())
        return "Removed"
    else:
        return "Not in list"

print(removeword(word))