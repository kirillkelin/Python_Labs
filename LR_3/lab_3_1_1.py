import math


def reducer(fraction):
    numerator = int(fraction[0])
    denominator = int(fraction[1])
    common_divisor = math.gcd(numerator, denominator)
    return int(numerator / common_divisor), int(denominator / common_divisor)


def main():
    print("Введите числетель и знаменатель дроби:")
    m = input()
    n = input()
    p = 1
    while p > 0:
        p = 0
        while not (m.isdigit()):
            p = 1
            print("Некорректный ввод числителя, попробуйте снова: ")
            m = input()
        while not (n.isdigit()):
            p = 1
            print("Некорректный ввод знаменателя, попробуйте снова: ")
            n = input()
        while int(m) > int(n):
            p = 1
            print("Некорректный ввод, попробуйте снова: ")
            m = input()
            n = input()
        if p == 0:
            break
    numerator, denominator = reducer(tuple([m, n]))
    print(numerator, denominator)


if __name__ == "__main__":
    main()
