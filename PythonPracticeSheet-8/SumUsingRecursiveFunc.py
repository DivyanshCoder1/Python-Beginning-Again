num = int(input("Enter the num: "))

#Sum(n) = n + Sum(n-1)

def totalsum(num):
    if num == 0:
        return 0
    else:
        return num + totalsum(num-1)
    
print(totalsum(num))