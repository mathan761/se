def analyze_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # оставляем только буквы, цифры и пробелы
    clean = ''
    for ch in text:
        clean += ch if ch.isalnum() or ch == ' ' else ' '

    words = clean.split()
    total = len(words)

    # считаем вручную количество каждого слова
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # ищем самое частое слово
    most_word, most_count = '', 0
    for w, c in counts.items():
        if c > most_count:
            most_word, most_count = w, c

    print(f"Общее количество слов: {total}")
    print(f"Самое частое слово: «{most_word}» — {most_count} раз(а)")
    print("\nТоп-10 самых частых слов:")
    for w, c in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{w}: {c}")

# пример вызова
analyze_text('article.txt')
