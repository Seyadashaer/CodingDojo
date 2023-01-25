class Animal:
    def __init__(self, name, happiness = 10):
        self.name = name
        self.health = 0
        self.happiness = happiness

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

    def display_info(self):
        print("Animal Name:", self.name , ", Health Level:" , str(self.health), "Happiness Level:", str(self.happiness))


animal1 = Animal("Bobo")
animal1.feed().display_info()


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def walk(self):
        self.happiness += 5
        return self

    def display_info(self):
        super(Dog, self).display_info()


dog1 = Dog("Spot")
dog1.walk().display_info()



class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.health = 170

    def play(self):
        self.health -= 10
        return self

    def display_info(self):
        super(Cat, self).display_info()


Cat1 = Cat("Puff")
Cat1.play().display_info()


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_Dog(self, name):
        self.animals.append( Dog(name) )
    def add_Cat(self, name):
        self.animals.append( Cat(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_Dog("Nala")
zoo1.add_Dog("Simba")
zoo1.add_Cat("Rajah")
zoo1.add_Cat("Shere Khan")
zoo1.print_all_info()
