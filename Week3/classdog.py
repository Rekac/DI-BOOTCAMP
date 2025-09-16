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
