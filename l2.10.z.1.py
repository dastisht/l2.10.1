class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Chirp!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type.lower() == "dog":
            return Dog(**kwargs)
        elif animal_type.lower() == "cat":
            return Cat(**kwargs)
        elif animal_type.lower() == "bird":
            return Bird(**kwargs)
        else:
            raise ValueError("Invalid animal type. Supported types are 'dog', 'cat', and 'bird'.")

if __name__ == "__main__":
    animal_type = "dog"
    animal_name = "Buddy"
    dog = AnimalFactory.create_animal(animal_type, name=animal_name)
    print(f"{dog.name} says: {dog.speak()}")  