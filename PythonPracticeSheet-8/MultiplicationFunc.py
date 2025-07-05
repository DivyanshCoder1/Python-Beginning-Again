num = int(input("Enter the number: "))

def createTable(num):
    for i in range(10):
        print(num, "x", i+1, "=", num*(i+1))

createTable(num)