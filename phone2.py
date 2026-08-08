# child can nat access private memmber of the parent class

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor ")
        self.__price = price
        self. brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s = SmartPhone(2000, "Apple" , 13)
print(s.show())

for i in range(1,6):
    for j in range(i):
        print("*" ,end="")

    print()
num = int(input('enter a number'))
for i in range(num):
    for j in range(num-1):
        print("")
    for k in range(2*i -1):
        print("*",end="")
    print()
    

