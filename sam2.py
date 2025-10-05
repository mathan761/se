import random

def dice_game():
    roll = random.randint(1, 6)
    print(f"Выпало значение: {roll}")

    if roll in [5, 6]:
        print("Вы победили")
    elif roll in [3, 4]:
        dice_game()
    elif roll in [1, 2]:
        print("Вы проиграли")

if __name__ == '__main__':
    dice_game()