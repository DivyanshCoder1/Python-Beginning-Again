num = int(input("Enter the height: "))

for i in range(num):
    print("  "*(num-(i+1)), end="")
    print("* "*(2*i+1))
input()