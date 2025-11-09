class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Томаты еще не созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Помидоры проходят стадии: отсутствует → цветение → зеленый → красный")
        print("- Ухаживайте за кустом, пока все плоды не станут красными")
        print("- Собирайте урожай только после полного созревания")


# 1. Вызовите справку по садоводству
Gardener.knowledge_base()
print()

# 2. Создайте объекты классов TomatoBush и Gardener
bush = TomatoBush(3)
gardener = Gardener("Михаил", bush)

# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
gardener.work()
print("После первого ухода:")
for t in bush.tomatoes:
    print(f"Помидор {t._index}: {Tomato.states[t._state]}")
print()

# 4. Попробуйте собрать урожай, когда томаты еще не дозрели
gardener.harvest()
print()

# Продолжайте ухаживать за ними
gardener.work()
gardener.work()
print("После полного созревания:")
for t in bush.tomatoes:
    print(f"Помидор {t._index}: {Tomato.states[t._state]}")
print()

# 5. Соберите урожай
gardener.harvest()