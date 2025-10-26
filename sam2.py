def expense_tracker():
    filename = 'expenses.txt'

    while True:
        print("\n=== УЧЕТ РАСХОДОВ ===")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Выход")
        choice = input("Выберите действие (1-3): ")

        if choice == '1':
            date = input("Введите дату (например 26.10.2025): ")
            category = input("Введите категорию расхода (например еда, транспорт): ")
            amount = input("Введите сумму расхода: ")
            description = input("Введите краткое описание: ")

            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"{date};{category};{amount};{description}\n")

            print("✅ Расход успешно добавлен!")

        elif choice == '2':
            print("\n=== СПИСОК РАСХОДОВ ===")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if not lines:
                        print("Пока нет записей.")
                    else:
                        total = 0
                        for line in lines:
                            date, category, amount, description = line.strip().split(';')
                            total += float(amount)
                            print(f"{date} | {category} | {amount} руб. | {description}")
                        print(f"\nИтого расходов: {total} руб.")
            except FileNotFoundError:
                print("Файл расходов ещё не создан.")

        elif choice == '3':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")
            

# Запуск программы
expense_tracker()
