import random

TYPE_FLOWERS = ['Rose', 'Lily', 'Peony', 'Tulip', 'Orchid', 'Aster']
COLORS = ['Yellow', 'Blue', 'White', 'Red', 'Pink', 'Purple']
COLORS_CUBE = ['blue', 'red', 'black', 'white']
LETTERS = ['d', 'e', 'r', 'y', 'u', 'm', 'p']


class Cube:

    def __init__(self):
        self.color = random.choice(COLORS_CUBE)
        self.letter = random.choice(LETTERS)

    def __repr__(self):
        return f"{self.color}|{self.letter}"


class Bag:
    bag = []

    def __init__(self):
        for cube in range(random.randint(10, 25)):
            c = Cube()
            self.bag.append(c)

    def random_add_cube(self):
        print(f"You pulled out a cube: {random.choice(self.bag)}")


class Animal:

    def __init__(self, animal, name, voice, color):
        self.animal = animal
        self.name = name
        self.voice = voice
        self.color = color

    def feed_animal(self, eat):
        print(f"{self.animal}, eating {eat} - om-nom-nom")

    def voice_animal(self):
        print(self.voice)

    def __repr__(self):
        return f"{self.animal}: {self.name}"


class Zoo:

    def __init__(self):
        pig = Animal('pig', 'Pepa', 'hru', 'pinky')
        lion = Animal('lion', 'Simba', 'rrr', 'golden')
        self.zoo = list()
        self.zoo.append(pig)
        self.zoo.append(lion)

    def get_animal(self):
        return random.choice(self.zoo)


zoo = Zoo()
animal = zoo.get_animal()
animal.voice_animal()
print(animal)
animal.feed_animal('apple')
print(zoo.zoo)


class Flower:
    def __init__(self):
        self.flower = random.choice(TYPE_FLOWERS)
        self.color = random.choice(COLORS)

    def __repr__(self):
        return f"{self.flower}: {self.color}"


class FlowerBed:

    def __init__(self):
        self.flowerbed = []
        for i in range(len(TYPE_FLOWERS)):
            flower = Flower()
            self.flowerbed.append(flower)


flowerbed = FlowerBed()
print(flowerbed.flowerbed)
