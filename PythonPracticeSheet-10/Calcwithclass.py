class Calculator:
    def __init__(self, value):
        self.value = value
    
    def cube(self):
        return (self.value)**3
    
    def square(self):
        return (self.value)**2
    
    def square_root(self):
        return (self.value)**(1/2)

num = Calculator(4)
num1 = Calculator(5)

print(num.cube())
print(num.square())
print(num.square_root())

print(num1.cube())
print(num1.square())
print(num1.square_root())