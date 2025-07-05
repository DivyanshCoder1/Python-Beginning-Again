a = int(input("N1: "))
b = int(input("N2: "))
c = int(input("N3: "))
d = int(input("N4: "))

if a > b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
elif a==b or b==c or c==d or a==d or a==c or b==d:
    print("Two Numbers are equal")
else:
    print(d)


