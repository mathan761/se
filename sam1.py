class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

phone = Smartphone("Samsung", "Galaxy S23")
print(phone.brand)
print(phone.model)