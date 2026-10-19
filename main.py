class Animal:
    def __init__(self, name, age, weight, color, habitat):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.habitat = habitat
    def eat(self):
        print(self.name + " ест")
    def sleep(self):
        print(self.name + " спит")
class Reptile(Animal):
    def __init__(self, name, age, weight, color, habitat, is_venomous, length):
        super().__init__(name, age, weight, color, habitat)
        self.is_venomous = is_venomous
        self.length = length
    def crawl(self):
        print(self.name + " ползёт")
    def shed_skin(self):
        print(self.name + " сбрасывает кожу")
class Amphibian(Animal):
    def __init__(self, name, age, weight, color, habitat, jump_height, can_swim):
        super().__init__(name, age, weight, color, habitat)
        self.jump_height = jump_height
        self.can_swim = can_swim
    def jump(self):
        print(self.name + " прыгает на " + str(self.jump_height) + " см")
    def croak(self):
        print(self.name + " квакает")
snake = Reptile("Змея", 3, 5, "зелёная", "пустыня", True, 150)
crocodile = Reptile("Крокодил", 10, 200, "серый", "река", False, 300)
frog = Amphibian("Лягушка", 2, 1, "зелёная", "болото", 50, True)
newt = Amphibian("Тритон", 1, 1, "коричневый", "пруд", 10, True)
class ZooShow:
    def __init__(self):
        self.ticket_price = 500
        self.vip_price = 1000
    def start(self):
        print("Добро пожаловать в зоошоу")
        print("Обычный билет:", self.ticket_price, "сом.")
        print("VIP билет:", self.vip_price, "сом.")
        print()
        print("Какое шоу хотите?")
        print("1 - Пресмыкающиеся")
        print("2 - Земноводные")
        choice = input("Ваш выбор: ")
        if choice == "1":
            print("1 - Змея")
            print("2 - Крокодил")
            animal_choice = input("Выберите животное: ")
            if animal_choice == "1":
                animal = snake
            else:
                animal = crocodile
        else:
            print("1 - Лягушка")
            print("2 - Тритон")
            animal_choice = input("Выберите животное: ")
            if animal_choice == "1":
                animal = frog
            else:
                animal = newt
        print()
        print("Выберите билет:")
        print("1 - Обычный")
        print("2 - VIP")
        ticket = input("Ваш выбор: ")
        if ticket == "2":
            price = self.vip_price
            place = "VIP зона"
        else:
            price = self.ticket_price
            place = "обычная зона"
        print()
        print("===== ВАШ БИЛЕТ =====")
        print("ШОУ: " + animal.name.upper())
        print("Место:", place)
        print("Цена:", price, "сом.")
        print("======================")
        print()
        print("Шоу начинается")
        animal.eat()
        animal.sleep()
        if isinstance(animal, Reptile):
            animal.crawl()
            animal.shed_skin()
        else:
            animal.jump()
            animal.croak()
show = ZooShow()
show.start()