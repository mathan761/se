b = (i ** 2 for i in range(1, 6))
print(b)  # выводит не числа, а сам генератор списков

print('first')
for i in b:
    print(i)

print('second')
# из-за особенностей выражения генераторов,
# они не будут выводиться больше одного раза
for i in b:
    print(i)