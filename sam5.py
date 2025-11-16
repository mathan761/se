class NonPositiveError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Число должно быть положительным, получено: {value}")

def divide_by_number(x):
    if x <= 0:
        raise NonPositiveError(x)
    return 100 / x

def process_value(val):
    if val <= 0:
        raise NonPositiveError(val)
    print(f"Значение {val} успешно обработано")

if __name__ == '__main__':
    try:
        print(divide_by_number(10))
        print(divide_by_number(-5))
    except NonPositiveError as e:
        print("Ошибка:", e)

    try:
        process_value(25)
        process_value(0)
    except NonPositiveError as e:
        print("Ошибка:", e)