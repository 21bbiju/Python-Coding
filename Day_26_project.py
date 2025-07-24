class Dog:
    species = "Dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Blacky = Dog("Blacky", 3)
Thor = Dog("Thor", 5)

print("Blacky is a {}" .format(Blacky.species))
print("Thor is also a {}".format(Thor.species))

print("{} is {} years old".format( Blacky.name, Blacky.age))
print("{} is {} years old".format( Thor.name, Thor.age))
