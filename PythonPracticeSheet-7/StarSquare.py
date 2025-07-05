num = int(input("Enter the side: "))

print("* "*(num))

for i in range(num-2):
    print("* ", end = "")
    print("  "*(num-2), end="")
    print("*")

print("* "*(num))
input()
input()