class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self):
        print(f"Звонок с {self.brand} {self.model}")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling):
        super().__init__(brand, model, battery)
        self.cooling = cooling

    def turbo_mode(self):
        print(f"{self.model} TURBO ON — {self.cooling} кулер активирован!")

rog = GamingPhone("ASUS", "ROG Phone 8", 95, "AeroActive Cooler")
rog.call()
rog.turbo_mode()