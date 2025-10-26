with open('input.txt', 'a+') as f:
    f.write('\n новая строка')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)