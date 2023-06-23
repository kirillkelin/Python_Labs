from Product import Product


class Production(Product):
    def __init__(self, product, amount):
        Product.__init__(self, product.name, product.price, product.width, product.height, product.length)
        self.__amount = amount
        self.__price_production = amount * product.price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    def final_price(self, discount):
        result = self.__price_production * (1 - discount / 100)
        if result < 0.01:
            return 0.01
        else:
            return float('{:.3f}'.format(result))

    def __str__(self):
        return "\n Production\n Amount: {} \t".format(self.__amount) + Product.__str__(self)

    def __add__(self, other):
        return self.__amount + other.__amount
