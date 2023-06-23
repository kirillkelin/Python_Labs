from Product import Product
from Production import Production
from Sale import Sale
import pickle


def inputInt():
    while True:
        n = input()
        try:
            n = float(n)
            if n < 0:
                raise Exception("Ошибка ввода! Число должно быть больше 0!")
            break
        except ValueError as e:
            print("Ошибка конвертации!")
        except Exception as e:
            print(e)
    return n


def inputStr():
    while True:
        n = input()
        try:
            if not (n.isalpha()):
                raise Exception("Ошибка ввода!")
            break
        except Exception as e:
            print(e)
    return n


def inputProduct():
    print("Введите объект: ")
    print("Введите имя объекта: ")
    name_product = inputStr()
    print("Введите цену объекта: ")
    price_product = inputInt()
    print("Введите ширину объекта: ")
    width_product = inputInt()
    print("Введите высоту объекта: ")
    height_product = inputInt()
    print("Введите длину объекта: ")
    length_product = inputInt()
    product = Product(name_product, price_product, width_product, height_product, length_product)
    return product


def main():
    filename = "Products"
    try:
        with open(filename, "rb") as file:
            my_list = pickle.load(file)
            for i in my_list:
                print(i)
    except Exception as e:
        print(e)
        my_list = []
    product1 = inputProduct()
    my_list.append(product1)
    product2 = inputProduct()
    my_list.append(product2)
    product3 = inputProduct()
    my_list.append(product3)
    try:
        with open(filename, "wb") as file:
            pickle.dump(my_list, file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
