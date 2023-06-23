print("Введите целое положительное число строк: ")
n = int(input())
while n < 0:
    print("Попробуйте ввести снова:")
    n = int(input("Введите целое положительное число строк:"))
my_dict = {}
print("Введите ряд, место, стоимость билета через пробел: ")
for i in range(0, n):
    temp = input().split()
    elements = [int(i) for i in temp]
    p = 1
    while p > 0:
        p = 0
        for i in elements:
            if i < 0:
                print("Ошибка, есть отрицательные числа. Введите снова:")
                p = 1
                break
        if p == 0:
            break
        temp = input().split()
        elements = [int(i) for i in temp]

    if (elements[0], elements[1]) in my_dict:
        my_dict[(elements[0], elements[1])].add(elements[2])
    else:
        my_dict[(elements[0], elements[1])] = set()
        my_dict[(elements[0], elements[1])].add(elements[2])
for keys in my_dict.keys():
    print(keys[0], keys[1], "-", len(my_dict[keys]))

