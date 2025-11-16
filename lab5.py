class SiteChecker:
    def __init__(self, func):
        print(f"Класс SiteChecker метод __init__ успешно запущен")
        self.func = func

    def __call__(self, *args):
        print(f"Функция перед запуском", self.func.__name__)
        self.func()
        print(f"Проверка безопасного выполнения")

@SiteChecker
def site():
    print("Успешная работа сайта")

if __name__ == "__main__":
    print("--- Сайт запущен ---")
    site()
    print("Сайт выключен")