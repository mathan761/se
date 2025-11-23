def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b



print("Первые 10 чисел Фибоначчи:")
for i, num in enumerate(fib(10), 1):
    print(f"{i}-е: {num}")

fib_200 = list(fib(200))[-1]
print("\n200-е число Фибоначчи:")
print(fib_200)