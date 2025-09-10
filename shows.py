from datetime import date
from voucher import *

from vip_ticket import VipTicket


class Shows:
    __id_counter = 1


    def __init__(self, show_name, show_date:date, tickets=None, food_vouchers=None):
        self.show_id = Shows.__id_counter
        Shows.__id_counter +=1
        self.show_name = show_name
        self.show_date = show_date
        self.tickets =  []
        self.vouchers = {}

    def add_ticket(self, ticket):
        if ticket in self.tickets:
            raise Exception('This ticket is already registered')
        self.tickets.append(ticket)

    def remove_ticket(self, ticket):
        if ticket not in self.tickets:
            raise Exception('This ticket not registered')
        self.tickets.remove(ticket)

    def show_revenue(self):
        return sum(ticket.calculate_price() for ticket in self.tickets)

    def total_discount(self):
        total_discount = 0
        for ticket in self.tickets:
            if isinstance(ticket, VipTicket):
                discount = ticket.customer.discount or 0
                total_discount += discount
        return total_discount


