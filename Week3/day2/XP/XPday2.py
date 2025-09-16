# import the Dog class
from classdog import Dog

class PetDog(Dog):    
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        dog1 = Dog("Rex", 6, 25)
        dog2 = Dog("June", 1, 10)
        dog3 = Dog("Nat", 3, 18)
        dogs = [dog1.name, dog2.name, dog3.name]
        print(f"{self.name} and {', '.join(dogs)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
    

