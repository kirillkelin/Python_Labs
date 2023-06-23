def poisk():
    while True:
        try:
            numbers = input("Введите последовательность целых чисел через пробел: ").split()
            for i in numbers:
                i = int(i)
            break
        except ValueError as e:
            print("Некорректный ввод!")

    while True:
        print("Введите целое число x:")
        try:
            x = int(input())
            break
        except ValueError as e:
            print("Некорректный ввод!")
    numbers = [int(i) for i in numbers]
    result = []
    for i in range(0, len(numbers) - 1):
        summa = numbers[i]
        result.append(numbers[i])
        for j in range(i + 1, len(numbers)):
            summa += numbers[j]
            result.append(numbers[j])
            if summa == x:
                return result
        result.clear()
    return False


def main():
    print(poisk())


if __name__ == '__main__':
    main()
