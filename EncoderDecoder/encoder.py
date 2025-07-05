import random
def encoder(user_string):
    splitted_string = user_string.split()
    random_letter_list = "ABCDEFGHIJKLMNOPQRSWTUVWXYZabcdefghijklmnopqrstuvwxyz"
    encoded_list = []

    for i in range(len(splitted_string)):
        if len(splitted_string[i]) < 3:
            final_string = splitted_string[i][::-1]
            encoded_list.append(final_string)
        elif len(splitted_string[i]) >= 3:
            string_list = list(splitted_string[i])
            first_letter = string_list[0]
            del string_list[0]
            string_list.append(first_letter)
            for j in range(3):
                string_list.insert(j, random.choice(random_letter_list))
                string_list.insert(len(string_list), random.choice(random_letter_list))
                string2 = "".join(string_list)
            encoded_list.append(string2)
    encoded_string = " ".join(encoded_list)
    return encoded_string
