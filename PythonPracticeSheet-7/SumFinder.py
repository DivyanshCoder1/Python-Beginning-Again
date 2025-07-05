import time
num = int(input("Enter the num: "))

mysum = 0
i = 1
while True:
    mysum += i
    i+=1
    if i == num+1:
        break
print(mysum)
input()