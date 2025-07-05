#More logical way
def printpyramid(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")
        print("#"*(i+1))
# printpyramid(5)

def printdblpyramid(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")
        print("#"*(i+1), end=" ")
        print("#"*(i+1), end="")
        for k in range(height-i):
            if k == height-i-1:
                print(" ")
            else:
                print(" ", end="")
# printdblpyramid(5)
#Easy way

def printpyramideasy(height):
    for i in range(height):
        print(" "*(height-i-1), end="")
        print("#"*(i+1))

# printpyramideasy(5)

def printdblpyramideasy(height):
    for i in range(height):
        print(" "*(height-i-1), end="")
        print("#"*(i+1), end=" ")
        print("#"*(i+1), end="")
        print(" "*(height-i-1))

# printdblpyramideasy(5)

