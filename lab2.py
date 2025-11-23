class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        self.count -= 1
        return self.count

if __name__ == "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)