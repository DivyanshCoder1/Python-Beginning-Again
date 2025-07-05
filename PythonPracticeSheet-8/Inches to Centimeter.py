num = int(input("Enter the value in inches: "))

def inchtocm(num):
    if num >=0:
        return num * 2.54
    else:
        return "Invalid Value"

print(inchtocm(num))