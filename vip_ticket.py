from ticket import Tickets as Tic
from customer import Customer, CustomerType


class VipTicket(Tic):
    def __init__(self,show_name,show_date,row_number,sit_number,customer:Customer, ticket_price):
        super().__init__(show_name,show_date,row_number,sit_number,customer, ticket_price)

    def calculate_price(self):
        if self.customer.customer_type!= CustomerType.VIP:
            raise Exception("Only VIP customers can buy VIP tickets!")
        if self.customer.discount:
            return self.ticket_price - self.customer.discount
        return self.ticket_price

    def get_ticket_type(self):
        return "vip"



