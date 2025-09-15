class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    ''' class of Cats and gives name and age as properties and print message of wals as bhavior'''   
    is_lazy = True

    def __init__(self, name, age):
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
Bengal1= Bengal("Panky", 6)
Chartreux2 = Chartreux("July", 2)
Siamese3 = Siamese("Leila", 1)  

all_cats = [Bengal1, Chartreux2, Siamese3]
sara_pets=Pets(all_cats)
sara_pets.walk


          

     
        

              

    

