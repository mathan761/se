class Smartphone:
    def __init__(self, brand, model):
        self._brand = brand      # protected
        self.__model = model     # private

    def boot(self):
        print(f"Загрузка {self._brand}")

phone = Smartphone("Google", "Pixel 9")
print(phone._brand)          # OK
# print(phone.__model)       # ERROR
phone.boot()