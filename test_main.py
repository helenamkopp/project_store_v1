import unittest
from main import Client, Payment, Product


class TestMain(unittest.TestCase):

    def setUp(self):
        self.product_1 = Product("Blouse", 250.00, "money")
        self.product_2 = Product("Pants", 190.00, "credit", 3)
        self.product_3 = Product("Jacket", 625.50, "credit", 8)
        self.product_4 = Product("Shoes", 325.75, "debit")
        self.product_5 = Product("Bikini", 65.80, "credit", 1)

        self.client_1 = Client("Isabel", "222.222.222-22", self.product_1)
        self.client_2 = Client("Maria", "777.555.111-65", self.product_2)
        self.client_3 = Client("Gabriel", "111.333.666-41", self.product_3)
        self.client_4 = Client("Mariana", "666.555.777-10", self.product_4)
        self.client_5 = Client("Lucia", "444.444.444-44", self.product_5)

    def tearDown(self):
        pass

    def test_apply_discount(self):
        self.product_1.apply_discount()

        self.assertEqual(self.product_1._price, 200.00)
        self.assertIsNot(self.product_1._price, 300.00)

    def test_apply_interest(self):

        self.assertEqual(self.product_2.apply_interest(), 199.50)
        self.assertEqual(self.product_3.apply_interest(), 688.05)
        self.assertEqual(self.product_4.apply_interest(), 325.75)
        self.assertEqual(self.product_5.apply_interest(), 65.80)

    def test_client_name(self):

        self.assertEqual(self.client_1._name_client, "Isabel")
        self.assertIsNot(self.client_2._name_client, "Helena")
        self.assertEqual(self.client_3._name_client, "Gabriel")

    def test_payment_installments(self):

        self.assertEqual(self.product_1._payment_installments, 0)
        self.assertEqual(self.product_2._payment_installments, 3)
        self.assertIsNot(self.product_3._payment_installments, 7)
        self.assertEqual(self.product_4._payment_installments, 0)





if __name__ == "__main__":
    unittest.main()
