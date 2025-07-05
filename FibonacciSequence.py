def f(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    else:
        N = f(n-1) + f(n-2)
        return N
# for calculation the whole sequence    

user_number = int(input("Number of terms: "))
for i in range(0, user_number):
    print(f(i), end=",")

#for nth term