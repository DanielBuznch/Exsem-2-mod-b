from datetime import date
from customer import Customer, CustomerType
from vip_ticket import VipTicket
from regular_ticket import Regular
from voucher import PizzaVoucher, SushiVoucher
from shows import Shows

if __name__ == "__main__":

    # ---- יצירת מופע ----
    concert = Shows("Rock Concert", date(2025, 9, 12))

    # ---- יצירת לקוחות ----
    john = Customer("John", "Doe", "john@example.com", "NY", CustomerType.VIP, discount=20)
    jane = Customer("Jane", "Smith", "jane@example.com", "LA", CustomerType.REGULAR)

    # ---- יצירת שוברים ----
    pizza = PizzaVoucher()
    sushi = SushiVoucher()

    # ---- נתינת שוברים ----
    john.give_food_voucher(pizza, concert)
    print("Vouchers after giving John:", concert.vouchers)

    jane.give_food_voucher(sushi, concert)
    print("Vouchers after giving Jane:", concert.vouchers)

    # ---- ניסיון לתת שוב שובר ל-John שוב (צריך לזרוק Exception) ----
    try:
        john.give_food_voucher(sushi, concert)
    except Exception as e:
        print("Expected Exception:", e)

    # ---- יצירת כרטיסים ----
    vip_ticket1 = VipTicket("Rock Concert", date(2025, 9, 12), 1, 1, john, 100)
    regular_ticket1 = Regular("Rock Concert", date(2025, 9, 12), 1, 2, jane, 50)

    # ---- הוספת כרטיסים למופע ----
    concert.add_ticket(vip_ticket1)
    concert.add_ticket(regular_ticket1)

    # ---- הצגת הכנסות והנחות ----
    print("Total revenue:", concert.show_revenue())
    print("Total VIP discount given:", concert.total_discount())
