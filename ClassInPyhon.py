#  # Creating a simple class
# class Dog:
#     # Attribute
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.age = 0
#         self.color = "brown"

#     # Method
#     def bark(self):
#         print(f"{self.name} (a {self.breed}) is barking: Woof Woof!")
    
#     def eat(self, food):
#         self.bark()
#         self.eat(food)

# # Instance
# # Creating an object
# dog1 = Dog("Bobby", "Bulldog") => {name: "Bobby", breed: "Bulldog"}
# dog2 = Dog("Max", "Bulldog") => {name: "Max", breed: "Bulldog"}

# print(dog1.name)  # Output: Bobby
# print(dog1.breed)  # Output: Bulldog

# class Human:
#     # static attributes
#     height = 0
#     weight = 0

#     def __init__(self, name, age, year):
#         # instance attributes
#         self.name = name
#         self.age = age
#         self.hobbies = []
#         self.gender = ""
#         self.title = "Ms"
#         self.year_of_birth = year

#     # Method
#     def eat(self, food):
#         print(f"{self.name} is eating {food}.")

#     def sleep(self, hours):
#         print(f"{self.name} is sleeping for {hours} hours.")

#     def drink(self, drink):
#         print(f"{self.name} is drinking {drink}.")
    
#     def calculate_age(self, target_year):
#         return int(target_year) - int(self.year_of_birth)
    

#     @staticmethod
#     def get_height(a = 0):
#         return Human.height + a


# student1 = Human("Uyen Minh", 12, 2012)
# student2 = Human("Nguyen Minh", 12, 2012)
# print(Human.get_height(10))
# print(student1.name, "\t", student1.age, "\t", student1.year_of_birth, "\t", student1.height)
# student1.height = 1
# Human.height = 1.5
# print(student1.name, "\t", student1.age, "\t", student1.year_of_birth, "\t", student1.height)
# print(student2.name, "\t", student2.age, "\t", student2.year_of_birth, "\t", student2.height)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

dog.make_sound()
cat.make_sound() 