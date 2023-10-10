class Animals():
    def __init__(self, name, type, legs, color):
        print("Called Constructor")
        self.name = name
        self.type = type
        self.legs = legs
        self.color = color

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    def sound(self):
        print("Sounds")

    def movement(self):
        print("Movement")


    def get_basic_characteristics(self):
        return [self.name, self.type, self.color, self.legs]

class WildAnimals(Animals):
    def __init__(self,name, type, legs, color, hunting):
        super().__init__(name, type, legs, color)
        self.hunting = hunting


    def hunting_behavior(self):
        print(f"Wolves are hunting on {self.hunting}")

    def get_basic_characteristics(self):
        super().get_basic_characteristics()
        print(super().get_basic_characteristics())
        print("Hunting....")

Wolf = WildAnimals("wolf", "mammel", 4, "grey", "animals")
Wolf.get_basic_characteristics()
Wolf.hunting_behavior()

class DomesticAnimals(Animals):
    def __init__(self, name, type, legs, color, feeding):
        super().__init__(name, type, legs, color)
        self.feeding = feeding

    def how_to_feed_an_animal(self):
        print(f"Cows are eating {self.feeding}")


    def get_basic_characteristics(self):
        super().get_basic_characteristics()
        print("Feeding...")

Cow = DomesticAnimals("cow", "mammel",4, "Black and White", "grass")
Cow.how_to_feed_an_animal()