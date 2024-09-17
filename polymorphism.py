class Animal:
    def make_sound(self):
        return "Some sound"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())
# Output:
# Meow!
# Bark!
