class Payment:

    def __init__(self, form_of_payment, payment_installments=0):
        self._form_of_payment = str(form_of_payment)
        self._payment_installments = int(payment_installments)


class Product(Payment):

    def __init__(self, name_product, price, form_of_payment, payment_installments=0):
        super().__init__(form_of_payment, payment_installments)

        if self._form_of_payment != "money" and self._form_of_payment != "credit" and self._form_of_payment != "debit":
            raise NameError(f"form_of_payment must be money or credit or debit not {self._form_of_payment}")

        self._name_product = str(name_product)
        self._price = float(price)

    def apply_discount(self):
        if self._form_of_payment == "money":
            self._price -= self._price * 0.20
            return self._price
        else:
            return False

    def apply_interest(self):
        if self._form_of_payment == "credit" and self._payment_installments <= 2 or self._form_of_payment == "debit":
            new_price = self._price

        elif self._form_of_payment == "credit" and self._payment_installments <= 4:
            new_price = self._price * 1.05

        elif self._form_of_payment == "credit" and self._payment_installments >= 5:
            new_price = self._price * 1.10

        return float(f"{new_price:.2f}")


class Client:

    def __init__(self, name_client, cpf, product):
        if not isinstance(product, Product):
            raise TypeError(f"product must be of type Product not {type(product)}")

        self._name_client = str(name_client)
        self._cpf = str(cpf)
