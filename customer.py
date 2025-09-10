from enum import Enum
from voucher import *
class CustomerType(Enum):

    REGULAR = 'REGULAR'
    VIP = 'VIP'


class Customer:
    __id_counter = 1
    __num_orders = 0

    def __init__(self, first_name, last_name, email, address, customer_type:CustomerType,voucher=None, discount=None):
        self.customer_id = Customer.__id_counter
        Customer.__id_counter += 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        if not isinstance(customer_type,CustomerType):
            raise Exception("customer_type must be a CustomerType Enum")
        self.customer_type = customer_type

        self.discount = discount
        self.voucher = voucher

    def give_food_voucher(self, voucher, show):
        if self.customer_id in show.vouchers:
            raise Exception(f"Customer {self.first_name} already has a voucher for this show")
        self.voucher = voucher
        show.vouchers[self.customer_id] = voucher.get_name()


    def take_food_voucher(self, show):
        if self.voucher:
            self.voucher = None
            if self.customer_id in show.vouchers:
                del show.vouchers[self.customer_id]

    def eat_food(self, show):
        if self.voucher is None or self.customer_id not in show.vouchers:
            raise Exception("No voucher to eat")
        self.voucher.eat()
        self.voucher = None
        del show.vouchers[self.customer_id]