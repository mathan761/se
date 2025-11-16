def add_two(number):
    try:
        result = 2 + int(number)
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two(5)
    add_two("abc")
    add_two(10.5)