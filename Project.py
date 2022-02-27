class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age


# These are two different dog objects
dog1 = Dog("Spot", 8, "Brown")
dog2 = Dog("Beefy", 4, "White")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(17)
dog2.change_age(9)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
