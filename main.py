class Product:

    def __init__(self, name_product, price):
        self._name_product = str(name_product)
        self._price = float(price)


class Payment:

    def __init__(self, form_of_payment):
        self._form_of_payment = str(form_of_payment)


class Client:

    def __init__(self, name_client, cpf, product, form_of_payment):
        if not isinstance(product, Product):
            raise TypeError(f"product must be of type Product not {type(product)}")

        if not isinstance(form_of_payment, Payment):
            raise TypeError(f"form_of_payment must be of type Payment not {type(form_of_payment)}")

        self._name_client = name_client
        self._cpf = cpf
    #
    #
    # def apply_discount(self):
    #     if self._form_of_payment == "money":
    #         self._price -= (self._price * 0.20)
    #
    #     elif self._form_of_payment == "credit card".strip().upper():
    #         self._price += (self._price + 1.05)
    #
    #     elif self._form_of_payment == "debit card".strip().upper():
    #         self._price -= (self._price * 0.05)
    #
    #
