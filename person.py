class person:
    def __init__(self, name, mood, money, health_rate="100%"):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    @staticmethod
    def sleep(hours):
        if hours == 7:
            person.mood = "happy"
        elif hours < 7:
            person.mood = "tired"
        elif hours > 7:
            person.mood = "lazy"

    @staticmethod
    def eat(meals):
        if meals == 3:
            person.health_rate = "100%"
        elif meals == 2:
            person.health_rate = "75%"
        elif meals == 1:
            person.health_rate = "50%"
        else:
            person.health_rate = "Unknown"

    @staticmethod
    def buy(items):
        person.money -= (items * 10)

    @staticmethod
    def display():
        print(f"your name is => {person.name}")
        print(f"your mode is => {person.mood}")
        print(f"your health rate is => {person.health_rate}")
        print(f"your remaining money is => {person.money} LE")


name = input("Enter your name: ").capitalize()
hours = int(input("Enter hours of sleep: "))
meals = int(input("Enter meals of day from 1 to 3: "))
money = int(input("Enter your money: "))
items = int(input("Enter items you buy: "))

print("*" * 100)
print((" " * 40) + "FROM PERSON CLASS")
print((" " * 25) + ("*" * 50))
person = person(name, "sad", money)
person.sleep(hours)
person.eat(meals)
person.buy(items)
person.display()


