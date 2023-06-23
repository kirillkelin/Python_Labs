import math


class Product:
    def __init__(self, name, price, width, height, length):
        self.__price = price
        self.__name = name
        self.__width = width
        self.__height = height
        self.__length = length

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def length(self):
        return self.__length

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, price):
        if price < 0.01:
            self.__price = 0.01
        else:
            self.__price = price

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    @length.setter
    def length(self, length):
        self.__length = length

    def final_price(self, discount):
        result = self.__price * (1 - discount / 100)
        if result < 0.01:
            return 0.01
        else:
            return float('{:.3f}'.format(result))

    def quantity(self, width, height, length):
        return math.floor(width * height * length / (self.__width * self.__height * self.__length))

    def __str__(self):
        return "Product:\nName: {} \tPrice: {} \tWidth: {} \tHeight: {}\tLength: {}".format(self.__name, self.__price,
                                                                                            self.__width, self.__height,
                                                                                            self.__length)

    def display_info(self):
        print(self.__str__())
