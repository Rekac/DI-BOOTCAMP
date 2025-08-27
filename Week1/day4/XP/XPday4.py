#ex1
my_fav_numbers ={3,5,7,10}
my_fav_numbers.add(35)
my_fav_numbers.add(42)
my_fav_numbers.remove(42)
print(my_fav_numbers)
friend_fav_numbers ={4,8,9,22,44,50}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#ex2 Tuple
my_tuple=(1,3,5,7,9)
new_tuple=(2,)
my_tuple+= new_tuple
print(my_tuple)

#ex3 List manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
basket.clear()
print(basket)

#ex4 Floats
my_list=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.]
new_list=[]
#loop to test all numbers if float and integer abd put only integer in my new_list
for a in my_list:
    if isinstance(a,int):
        new_list.append(a)
print(new_list)

#or
# newlist=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.]
#newlist = [x for x in newlist if type(x) != float]
#print(newlist)

#ex5 -write a loop to pritn the numbers 1 to 20
newlist = [x for x in range(1,21)]
print(new_list)
even_list=[x for x in newlist if x %2==1]
even_list.append(x)
print(even_list)

 #ex7
fruit = input("Enter items separated by commas: ")
item_list = fruit.split(',')
for item in item_list:
    print(item.strip()) 

#user input
user_input= input("Enter a fruit name: ")
if user_input in item_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#ex8  Pizza Topppings

while True:
    user_input = input("Enter a Pizza Topping: ")
    if user_input=="quit":
        break
    else:
        print(user_input)
        price=10+len(user_input)*2.5
        print(f'The price of pizza is{price}')