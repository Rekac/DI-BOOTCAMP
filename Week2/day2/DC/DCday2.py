#DC day2 
# create function that takes a number and multiplies from 1 to length
def generate_multiples(number, length):
    return [number * i for i in range(1, length + 1)]

number = int(input("please enter a number: "))
length = int(input("please enter the length: "))

print(generate_multiples(number, length))



    