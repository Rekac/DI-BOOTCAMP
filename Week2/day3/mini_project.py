def new_func(Fruits):

while True:
    Fruits = input("Enter your favorite fruits: ")
    if not Fruits:
        print("is empty")
        break
    new_func(Fruits)