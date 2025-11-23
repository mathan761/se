def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w", encoding="utf-8") as file:
        for i in range(1, n + 1):
            file.write(str(a) + "\n")
            if i == n:
                print(f"200-е число Фибоначчи: {a}")
            a, b = b, a + b


# Генерируем и записываем первые 200 чисел Фибоначчи
fib(200)

print("Все числа успешно записаны в файл fib.txt")