def analyze_file():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("Файл пуст.")
        return

    longest = max(lines, key=len)
    print(f"Количество строк в файле: {len(lines)}")
    print(f"Самая длинная строка ({len(longest.strip())} символов): {longest.strip()}")

analyze_file()
