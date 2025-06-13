def calcfact():
    num = input("Please enter the number: ")
    numnew = num
    try:
        num = int(num)
        numnew = int(numnew)
        if num < 0 :
            print("Invalid Number, Please reenter the value\n")
        if num == 0:
            print(1, "\n")
        if num > 0:
            for i in range(1, num):
                numnew = numnew*(num-i)
                # print(numnew)
            print(numnew, "\n")
    except:
        print("Please enter an integer\n")
    
    calcfact()
calcfact()


