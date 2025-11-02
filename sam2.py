class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self):
        print(f"Звонок с: {self.brand} {self.model}")

    def charge_level(self):
        print(f"Заряд: {self.battery}%")

phone = Smartphone("Apple", "iPhone 15", 89)
phone.call()
phone.charge_level()