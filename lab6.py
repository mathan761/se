def mean(data):
    return sum(data) / float(len(data))

def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Значение = {mean(j)}")

if __name__ == '__main__':
    main(X=[1, 2, 3], Y=[3, 3, 0])