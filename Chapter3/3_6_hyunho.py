from collections import deque
import unittest

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

    def getOrder(self):
        return self.order

    def setOrder(self, value):
        self.order = value

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.order = 0
        self.dogs = deque()
        self.cats = deque()

    def enqueue(self, animal):
        animal.setOrder(self.order)
        if isinstance(animal, Cat):
            self.cats.append(animal)
        elif isinstance(animal, Dog):
            self.dogs.append(animal)
        self.order += 1

    def dequeueAny(self):
        if len(self.cats) == 0:
            return self.dequeueDog()
        elif len(self.dogs) == 0:
            return self.dequeueCat()
        else:
            if self.cats[-1].getOrder() < self.dogs[-1].getOrder():
                return self.dequeueCat()
            else:
                return self.dequeueDog()

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.popleft().name

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.popleft().name


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAny()), "Garfield")
        self.assertEqual(str(shelter.dequeueDog()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Clifford")
        self.assertEqual(str(shelter.dequeueCat()), "Tony")
        self.assertEqual(str(shelter.dequeueCat()), "None")
        self.assertEqual(str(shelter.dequeueAny()), "Blue")
        self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
    unittest.main()
