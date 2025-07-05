def greet(fx):
    def mfx(*args, **kwargs):
        print("This should be printed first")
        print(fx(*args, **kwargs))
        print("This should be printed second")
    return mfx

@greet
def add(a,b):
    print("This is the function's print statement")
    print(a+b)

greet(add)(1,2)