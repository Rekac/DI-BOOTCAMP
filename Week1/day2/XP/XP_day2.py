#EX1 Print Hello  4 times
print("Hello " *4)
#EX2 Print calculation of (99^3)*8
calculation= (99**3)*8
print(calculation)
# other form is define the inputs 
#import math
#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#r=(pow(a,b)*c)
#print(int(r))

#EX3 Predict output of each condition
print(3==3)
print(3=='3') #error cause "3" is not int so needed to change to print(3==int('3'))
print(int("3")>3)
print("Hello"=="hello")

#EX4 Print your computer brand
computer_brand="lenovo" 
print('I have '+computer_brand+ ' computer')

#EX5 Print your information
name='Renta'
age= '25'
shoe_size='44'
info =f"Me name is " +name+ ", I am " +age+ " years old" " and my shoe size  is "+shoe_size+""
print(info)

#EX6 Print Hello World
a=5
b=3
if a>b:
    print("Hello World")
else:
    print(" ")
    #more flexible wy
#a= input("enter  numer: ")
#b= input("enter  numer: ")
#if a>b:
 #   print("Hello World")
#else:
#    print(" ")

#EX7 Print if the number is even or odd
if a%2==0:
    print("The number {} is even".format(a))
else:
    print("The number{} is odd".format(a))

#EX8 Comparing if names are the same
my_name='Renata'
user_name=input("Enter your name: ")
if my_name ==user_name:
    print("what a coincidence,we have the same name")
else:
    print("Nice to meet you "+user_name)
#EX9 Identify if it is tall enough to ride the roaller coaster
Height=int(input("Enteryour Height in cm: "))
if Height>=145 :
    print("you can ride the Roaller Coaster")
else:
    print("Sorry, you can't play the Roaller Coaster")