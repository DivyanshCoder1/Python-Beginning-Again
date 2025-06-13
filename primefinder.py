import math

num = int(input("Please enter the number: "))

for i in range(2, num):
    if num%i==0:
        print(f"{num} is not prime, it is divisible by {i}")
        continue