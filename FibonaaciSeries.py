number_list = [0,1]

user_input = int(input("Enter the number of terms: "))

for i in range(0, user_input):
    number_list.append(number_list[i] + number_list[i+1])
    print(number_list[i], end=",")