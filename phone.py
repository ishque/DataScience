class Phone:
    def __init__(self, price, brand,camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):
    pass


s = SmartPhone(29999, "Apple", 13)
s.buy()
print(s.price)
print(s.camera)
print(s.brand)
        