from abc import ABC, abstractmethod
from customer import Customer


class Tickets(ABC):
    __id_counter = 1
    @abstractmethod
    def __init__(self,show_name,show_date,row_number,sit_number,customer:Customer, ticket_price):
        self.ticket_id = Tickets.__id_counter
        Tickets.__id_counter += 1
        self.show_name = show_name
        self.show_date = show_date
        self.row_number = row_number
        self.sit_number = sit_number
        self.customer = customer
        self.ticket_price = ticket_price

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def get_ticket_type(self):
        pass