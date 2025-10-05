from datetime import datetime as dt
from datetime import timedelta as td

def main():
    today = dt.today()

    n = int(input('Введите количество дней: '))

    result = today + td(days=n)

    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели {dt.today().isoweekday()}"
    )

    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()