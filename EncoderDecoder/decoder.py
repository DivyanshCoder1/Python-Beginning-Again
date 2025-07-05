def decode(user_string):
    splitted_list = user_string.split()
    decoded_list = []

    for i in range(len(splitted_list)):
        if len(splitted_list[i]) < 3:
            final_string = splitted_list[i][::-1]
            decoded_list.append(final_string)
        elif len(splitted_list[i]) >= 3:
            string_list = list(splitted_list[i])
            for j in range(3):
                del string_list[0]
            for k in range(3):
                del string_list[len(string_list)-1]
            last_letter = string_list[len(string_list)-1]
            del string_list[len(string_list)-1]
            string_list.insert(0, last_letter)
            final_string = "".join(string_list)
            decoded_list.append(final_string)
    decoded_string = " ".join(decoded_list)
    return decoded_string
# print(decode("LTSivyanshDoEK si a eMDumanhxQy"))
# #LTSivyanshDoEK si a eMDumanhxQy

#ZzZello,HafB I ma nbSivyanshDWLn BnWandey,PunU I joyikelevf 2 Ttvce-creamsikvl
#Hello, I am WivyashD uadey,P I eikl 2 ice-creams
#Hello, I am Divyansh Pandey, I like 2 ice-creams