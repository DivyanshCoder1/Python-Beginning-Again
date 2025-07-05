a = int(input("Enter the number is Sub 1: "))
b = int(input("Enter the number is Sub 2: "))
c = int(input("Enter the number is Sub 3: "))

total_pass = 0.4*300
s1_pass = 33
s2_pass = 33
s3_pass = 33

total = a+b+c

if total >= total_pass:
    if a<s1_pass:
        print("Fail in Sub 1")
    elif b < s2_pass:
        print("Fail in Sub 2")
    elif c < s3_pass:
        print("Fail in Sub 3")
    else:
        print("Pass")
else:
    print("Fail")