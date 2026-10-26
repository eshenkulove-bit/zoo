from abc import ABC, abstractmethod
from datetime import date


class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_name(self):
        return self.name

    @abstractmethod
    def calculate_price(self):
        pass


class Pizza(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size

    def calculate_price(self):
        if self.size == "большая":
            return self.base_price * 1.3
        return self.base_price

    def get_name(self):
        return self.name + " (" + self.size + ")"


class Drink(MenuItem):
    def __init__(self, name, base_price, has_ice):
        super().__init__(name, base_price)
        self.has_ice = has_ice

    def calculate_price(self):
        return self.base_price

    def get_name(self):
        if self.has_ice:
            return self.name + " со льдом"
        return self.name


class ComboSet(MenuItem):
    def __init__(self, name):
        super().__init__(name, 0)
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def calculate_price(self):
        total = 0
        for dish in self.dishes:
            total = total + dish.calculate_price()
        return total * 0.85


class PaymentStrategy(ABC):
    # возвращает True, если оплата прошла, и False, если нет
    @abstractmethod
    def collect_payment(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def __init__(self, card_number, expire_month, expire_year):
        self.card_number = card_number
        self.expire_month = expire_month
        self.expire_year = expire_year

    def is_card_valid(self):
        if self.expire_month < 1 or self.expire_month > 12:
            return False

        today = date.today()
        if self.expire_year < today.year:
            return False
        # карта действует до конца месяца, указанного на ней
        if self.expire_year == today.year and self.expire_month < today.month:
            return False
        return True

    def collect_payment(self, amount):
        if not self.is_card_valid():
            print("Оплата не прошла: карта просрочена или срок указан неверно")
            return False

        print("С карты", self.card_number, "списано", amount, "сом")
        return True


class CashPayment(PaymentStrategy):
    def collect_payment(self, amount):
        print("Оплата наличными курьеру:", amount, "сом")
        return True


class Order:
    def __init__(self):
        self.__items = []
        self.__statuses = ["Создан", "Готовится", "Доставляется", "Доставлен"]
        self.__status_index = 0

    def add_item(self, item):
        if self.__status_index > 0:
            raise Exception("Нельзя добавить блюдо в заказ со статусом: " + self.get_status())
        self.__items.append(item)

    def next_step(self):
        if self.__status_index == len(self.__statuses) - 1:
            raise Exception("Заказ уже доставлен")
        self.__status_index = self.__status_index + 1

    def get_status(self):
        return self.__statuses[self.__status_index]

    def get_total_cost(self):
        total = 0
        for item in self.__items:
            total = total + item.calculate_price()
        # округляем, чтобы не было длинных хвостов вроде 442.00000000001
        return round(total, 2)

    def pay(self, payment_method):
        if len(self.__items) == 0:
            raise Exception("Заказ пустой, платить нечего")
        return payment_method.collect_payment(self.get_total_cost())


order = Order()

combo = ComboSet("Комбо обед")
combo.add_dish(Pizza("Маргарита", 400, "средняя"))
combo.add_dish(Drink("Сок", 120, False))

order.add_item(Pizza("Пепперони", 500, "большая"))
order.add_item(Drink("Кола", 100, True))
order.add_item(combo)

print("Итого:", order.get_total_cost())

order.next_step()
print("Статус:", order.get_status())

try:
    order.add_item(Drink("Чай", 80, False))
except Exception as error:
    print("Ошибка:", error)

if not order.pay(CardPayment("1234-5678", 1, 2020)):
    order.pay(CashPayment())

order.next_step()
print("Статус:", order.get_status())