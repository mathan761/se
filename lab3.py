a = [i ** 2 for i in range(1, 6)]
print(a)

for i in a:
    print(i)

print(iter(a))  # <list_iterator object at ...>
for i in a:
    print(i)