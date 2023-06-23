from Product import Product


class Sale(Product):
    def __init__(self, product, frequency_sale):
        Product.__init__(self, product.name, product.price, product.width, product.height, product.length)
        self.__frequency_sale = frequency_sale

    @property
    def frequency_sale(self):
        return self.frequency_sale

    @frequency_sale.setter
    def frequency_sale(self, frequency_sale):
        self.__frequency_sale = frequency_sale

    def __str__(self):
        return "\n Production\n Frequency_sale: {} \t".format(self.__frequency_sale) + Product.__str__(self)
