#ex1-define what you are learning 
def topic():
    print('I am learning about functions in Python')
topic()
#ex2 -Create a function that displays a message about a favorite book
def favorite_book(title):
    print('One of my favorite book is '+ title)
favorite_book('The Notebook')

#ex3-Create a function that describes a city and its country
def describe_city(city="Unknown",country="Unknown"):
    print(city +"is in"+ country)
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#ex4 Create a function that generates random numbers and compares them
# import library random
import random
def random_number(num1,num2)->int: 
    num1 = random.randint(1,100)
    num2 = int(input("Please enter a number: "))
    if num1==int(num2):
        print(f"Success!")
    else:
        print(f"Fail!Your number: {num2} random number: {num1}") 
random_number()

#ex5 
# Let’s Create Some Personalized Shirts
def make_shirt(size="Large",text="I love Python"):
    print(f'the size of the shirt is {size} and the text is {text}')
make_shirt()
make_shirt("medium")
make_shirt("small","custom")  


#ex6 Magicans
#Modify a list of magician names and display them in different ways
magicians_names = ['Harry Houdini', 'David Blaine','Criss Angel']

def show_magicioans(*args):
    for name in magicians_names:
     print(name)

show_magicioans()

def make_great(magicians_names):
 for name in magicians_names:
        print(f'the Great {name}')

make_great()
show_magicioans()


 





