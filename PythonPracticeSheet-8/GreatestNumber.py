def find_greatest(a,b,c):
    if a>b and b > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "Equal"

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
print(find_greatest(a,b,c))
input()