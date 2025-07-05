user_input = int(input("Enter your marks: "))

if 100>= user_input >=90:
    print("Ex")
elif 90>user_input>=80:
    print("A")
elif 80>user_input>=70:
    print("B")
elif 70>user_input>=60:
    print("C")
elif 60>user_input>=50:
    print("D")
else:
    print("F")