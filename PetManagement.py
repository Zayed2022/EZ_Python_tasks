class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_pet_type(self, pet_type):
        self.pet_type = pet_type

    def get_pet_type(self):
        return self.pet_type

if __name__ == "__main__":
    pet1 = Pet("Buddy", 3, "Dog")
    pet2 = Pet("Whiskers", 5, "Cat")
    print("Pet 1:")
    pet1.set_name("Max")
    print("Name:", pet1.get_name())
    print("Age:", pet1.get_age())
    print("Type:", pet1.get_pet_type())
    print("\nPet 2:")
    print("Name:", pet2.get_name())
    print("Age:", pet2.get_age())
    print("Type:", pet2.get_pet_type())
