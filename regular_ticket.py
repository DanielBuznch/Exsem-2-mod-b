from ticket import Tickets as Tic


class Regular(Tic):
    def __init__(self,show_name,show_date,row_number,sit_number,ticket_customer, ticket_price):
        super().__init__(show_name,show_date,row_number,sit_number,ticket_customer, ticket_price)

    def calculate_price(self):
        return self.ticket_price

    def get_ticket_type(self):
        return "REGULAR"


