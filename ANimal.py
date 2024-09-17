class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # To be implemented by subclasses

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

my_dog = Dog("Rex")
print(my_dog.make_sound())