class Weapon:
    def fire(self):
        pass

class Pistol(Weapon):
    def fire(self):
        return "Bang!"

class Rifle(Weapon):
    def fire(self):
        return "BANG-BANG-BANG!"

class Sniper(Weapon):
    def fire(self):
        return "BOOM!"

guns = [Pistol(), Rifle(), Sniper(), Pistol()]
for gun in guns:
    print(gun.fire())