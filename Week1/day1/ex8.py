while True:
    user_input = input("Enter a Pizza Topping: ")
    if user_input=="quit":
        break
    else:
        topping=user_input.split(',')
        for top in topping:
         print(top.strip()) 
         top1=0+len([top])   
        price = 10 + top1 * 2.5
        print(f'The price of pizza is {price}')