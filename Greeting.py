import time

#This is one way to get time and do the deed
localtime = time.localtime()

def telltime():
    if localtime.tm_hour > 12:
        print(f"The current time is {localtime.tm_hour-12}:{localtime.tm_min}:{localtime.tm_sec}")
    else:
        print(f"The current time is {localtime.tm_hour}:{localtime.tm_min}:{localtime.tm_sec}")


if 5 <= localtime.tm_hour < 12:
    print("Good Morning")
    telltime()
elif 12 <= localtime.tm_hour < 16:
    print("Good Afternoon")
    telltime()
elif 16 <= localtime.tm_hour < 22:
    print("Good Evening")
    telltime()
else:
    print("Good Night")
    telltime()


#This is supposed to be the other way to do the same thing

# hour = time.strftime("%H")
# minutes = time.strftime("%M")
# sec = time.strftime("%S")
# print("The current time is", end=" ")
# if int(hour) > 12:
#     print(f"{int(hour)-12}:{minutes}:{sec}")
# else:
#     print(f"{hour}:{minutes}:{sec}")
