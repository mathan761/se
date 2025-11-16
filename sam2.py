class EmptyFileError(Exception):
    pass

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                raise EmptyFileError("файл пустой")
            print(content)
    except EmptyFileError as e:
        print(e)
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == '__main__':
    read_file("empty.txt")
    read_file("data.txt")