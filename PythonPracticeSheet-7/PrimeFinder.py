import math

num = int(input("Enter the number: "))

def primecheck(num):
    for i in range(2,math.floor(num ** (1/2)) + 1):
        if num % i == 0:
            print("Divisible by", i)
            return False
    return True

if primecheck(num):
    print("The number is prime!")
else:
    print("Not Prime!")
input()