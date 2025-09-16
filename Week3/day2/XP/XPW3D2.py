class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
         print(animal.walk)

class Cat():

    is_lazy = True

    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

class Siamese(Cat):
    pass

 #CREATE A LIST

Bengal_obj= Bengal("Panky", 6)
Chartreux_obj = Chartreux("July", 2)
Siamese_obj = Siamese("Leila", 1) 
all_cats = [Bengal_obj, Chartreux_obj, Siamese_obj]

sara_pets=Pets(all_cats)
sara_pets.walk

#EX2 Create a Dog class with methods for barking, running speed, and fighting

class Dog:
    def __init__(self, name, age,weight):
        self.name=name 
        self.age=age
        self.weight=weight
        

    def bark(self):
        return "Is barking"
    
    def run_speed(self):
        speed =float(self.weight / self.age * 10)
        return speed

    def fight(self, other_dog):
        self_score = self.run_speed() * (self.weight)
        other_score = other_dog.run_speed() * (other_dog.weight)
    
        if self_score > other_score:
            return f"{self.name} wins!"
        elif self_score < other_score:
            return f"{other_dog.name} wins!"
        else:
            return "It's a tie!"
        

dog1=Dog("Rex",6,25)
dog2=Dog("June",1,10)
dog3=Dog("Nat",3,18)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
    
#EX3    