from abc import ABC,abstractmethod

class FoodVoucher(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def eat(self):
        print("Here is your food, enjoy!")




class PizzaVoucher(FoodVoucher):
    def get_name(self):
        return "Pizza"

    def eat(self):
        super().eat()


class SushiVoucher(FoodVoucher):
    def get_name(self):
        return "Sushi"

    def eat(self):
        super().eat()


class BurgerVoucher(FoodVoucher):
    def get_name(self):
        return "Burger"

    def eat(self):
        super().eat()


class SaladVoucher(FoodVoucher):
    def get_name(self):
        return "Salad"

    def eat(self):
        super().eat()
