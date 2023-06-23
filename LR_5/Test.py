from unittest import TestCase, main
from Product import Product
from Production import Production


class final_price1Test(TestCase):
    def testdefault1(self):
        product1 = Product("Конфеты", 2500, 30, 40, 50)
        self.assertEqual(product1.final_price(20), 2000)

    def testdefault2(self):
        product1 = Product("Пирожки", 2500, 30, 40, 50)
        self.assertEqual(product1.final_price(30), 1750)

    def testdefault3(self):
        product1 = Product("Пирожные", 2500, 30, 40, 50)
        self.assertEqual(product1.final_price(40), 1500)

    def testdefault4(self):
        product1 = Product("Торты", 2500, 30, 40, 50)
        self.assertEqual(product1.final_price(50), 1250)

    def testdefault5(self):
        product1 = Product("Эклеры", 2500, 30, 40, 50)
        self.assertEqual(product1.final_price(35), 1625)


class quantityTest(TestCase):
    def testdefault1(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        self.assertEqual(product1.quantity(30, 40, 50), 1000)

    def testdefault2(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        self.assertEqual(product1.quantity(40, 50, 60), 2000)

    def testdefault3(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        self.assertEqual(product1.quantity(50, 60, 70), 3500)

    def testdefault4(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        self.assertEqual(product1.quantity(15, 20, 25), 125)

    def testdefault5(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        self.assertEqual(product1.quantity(18, 20, 22), 132)

class final_price2Test(TestCase):
    def testdefault1(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        production1 = Production(product1, 10)
        self.assertEqual(production1.final_price(25), 18750)

    def testdefault2(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        production1 = Production(product1, 20)
        self.assertEqual(production1.final_price(25), 37500)


    def testdefault3(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        production1 = Production(product1, 7)
        self.assertEqual(production1.final_price(25), 13125)

    def testdefault4(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        production1 = Production(product1, 13)
        self.assertEqual(production1.final_price(25), 24375)

    def testdefault5(self):
        product1 = Product("Конфеты", 2500, 3, 4, 5)
        production1 = Production(product1, 3)
        self.assertEqual(production1.final_price(25), 5625)