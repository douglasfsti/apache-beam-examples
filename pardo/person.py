class Person(object):
    def __init__(self, name, age=18, lucky_number=42, drink="water"):
        self.name = name
        self.age = age
        self.lucky_number = lucky_number
        self.drink = drink

    def __str__(self):
        return "%s;%s;%s;%s" % (self.name, self.age, self.lucky_number, self.drink)
