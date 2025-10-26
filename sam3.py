def text_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    letters = 0
    for ch in text:
        if ('a' <= ch.lower() <= 'z'):
            letters += 1

    words = text.split()
    word_count = len(words)


    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)

    print(f"Input file contains:\n{letters} letters\n{word_count} words\n{line_count} lines")

# запуск программы
text_stats('input.txt')
