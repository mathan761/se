from module import area

def main():
    print("Расчет площади треугольника")
    

    side_a = float(input("Введите длину стороны a: "))
    side_b = float(input("Введите длину стороны b: "))
    side_c = float(input("Введите длину стороны c: "))

    calc_area = area(side_a, side_b, side_c)
    
    print(f"\nДлины сторон: a={side_a}, b={side_b}, c={side_c}")
    print(f"Полученная площадь треугольника: {calc_area:.2f}")
        


if __name__ == '__main__':
    main()