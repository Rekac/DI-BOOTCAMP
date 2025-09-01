while True:
    user_input = input("Enter a Pizza Topping: ")
    if user_input=="quit":
        break
    else:
        print(user_input)
        price=10+len(user_input)*2.5
        print(f'The price of pizza is{price}')



 def price(number, length):
    return [number * i for i in range(1, length + 1)]

user_input = input("please enter a Topping: ")
mylist=user_input.split()
print(mylist)