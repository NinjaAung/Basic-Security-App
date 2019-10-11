from datetime import datetime
from bcrypt import hashpw, gensalt

class User(object):
    def __init__(self, email, password='None'):
        self.email = email  # email will be the username
        self.password = hashpw(password.encode(
            'utf-8'), gensalt())  # encrypt password
        self.timestamp = datetime.now()  # creation time stamp
        self.cart = []  # empty list of items
        self.is_active = False
        self.corn_list = []

    def get_email(self):
        return self.email

    def get_timestamp(self):
        return self.timestamp

    def json(self):
        return {
            'email': self.email,
            'password': self.password,
            'created_at': self.timestamp,
            'cart': self.cart,
            'corn_list': self.corn_list

        }

    def add_to_cart(self, Corn):
        self.cart.append(Corn)


class Corn(object):
    def __init__(self, name, src, cost):
        self.path = src
        self.name = name
        self.cost = cost

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def json(self):
        return {
            'src': self.path,
            'name': self.name,
            'cost': self.cost
        }