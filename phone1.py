class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram

        print("Inside SmartPhone Constructor")


s = SmartPhone("Andorid", 2)
print(s.brand)
print(s.camera)