import random


class Cube:
    colors = ['blue', 'red', 'black', 'white']
    letters = ['d', 'e', 'r', 'y', 'u', 'm', 'p']

    def __init__(self):
        self.color = random.choice(self.colors)
        self.letter = random.choice(self.letters)

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

    def __init__(self, animal, name, voice, color, eat=0):
        self.animal = animal
        self.name = name
        self.voice = voice
        self.color = color
        self.eat = eat

    def feed_animal(self, eat):
        self.eat += eat

    def voice_animal(self):
        print(self.voice)


class Zoo:
    def __init__(self):
        self.zoo = {}

    def add_animal_zoo(self, animal):
        self.zoo.setdefault(animal.animal, {'name': animal.name, 'voice': animal.voice, 'color': animal.color})


pig = Animal('pig', 'Pepa', 'hru', 'pinky')
lion = Animal('lion', 'Simba', 'rrr', 'golden')
zoo = Zoo()
zoo.add_animal_zoo(pig)
zoo.add_animal_zoo(lion)
print(zoo.zoo)
print(pig.voice)


class Flower:
    type_flowers = ['Rose', 'Lily', 'Peony', 'Tulip', 'Orchid', 'Aster']
    colors = ['Yellow', 'Blue', 'White', 'Red', 'Pink', 'Purple']

    def __init__(self):
        self.flower = dict()
        self.flower[random.choice(self.type_flowers)] = random.choice(self.colors)


class FlowerBed:

    def __init__(self):
        self.flowerbed = {}
        for i in range(len(Flower.type_flowers)):
            flower = Flower()
            for key, values in flower.flower.items():
                self.flowerbed.setdefault(key, {'color': values})


flowerbed = FlowerBed()
print(flowerbed.flowerbed)
