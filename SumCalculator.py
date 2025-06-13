#Using for loops, damn long but good for leanrning and logic building
num1 = int(input("Please enter the number from which you want to start sum: "))
num2 = int(input("Please enter the number at which you want to end sum: "))
numnew = num1
print(int(num1), end=" ")

for i in range(1, int(num2) - int(num1)+1):
    numnew = int(numnew) + (int(num1) + i)
    print("+", int(num1)+i, end=" ")
print()
print(numnew)


#Method 2, direct shit, more of a common sense

Snum1 = int(num1*(num1+1)/2)
Snum2 = int(num2*(num2+1)/2)

print(int(Snum2-Snum1 + num1))