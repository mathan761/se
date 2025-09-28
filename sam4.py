def analyze_text(text : str):
    print(f'Длина предложения. {len(text)}')

    lower_case = text.lower()
    print(f"В нижнем регистре: {lower_case}")

    count_letters = 0
    for letter in text:
        if letter in "aeiou":
            count_letters+=1
    print(f"Количество гласных: {count_letters}")

    beauty_text = text.replace('ugly','beauty')
    print(f"Замена ugly на beauty {beauty_text}")

    starts_with_the = text.startswith("The")
    ends_with_end = text.endswith("end")
    print(f"Начинается с 'The': {starts_with_the}")
    print(f"Заканчивается на 'end': {ends_with_end}")


test1 = "The ugly Dog came to the end."
print(f"Тест 1 (Ввод): {test1}")
analyze_text(test1)

test2 = "This is another sentence."
print(f"Тест 2 (Ввод): {test2}")
analyze_text(test2)

test3 = "Ugly is an ugly word."
print(f"Тест 3 (Ввод): {test3}")
analyze_text(test3)