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
toppings = []
while True:
    user_input = input("Please enter a topping (or 'quit' to finish): ")
    if user_input() == 'quit':
        break
    toppings.append(user_input)
    print(f"Added {user_input} to your pizza.")

print("Your toppings:", toppings)
price = 10 + len(toppings) * 2.5
print(f"The price of the pizza is ${price}")

#ex9 Cinema Tickets
users=[]
cost=[]
new_users=[]
new_cost=[]
while True:
    user_input = input("Please enter your namere (or ' ' to finish): ")
    age_input = input("Please enter an age (or ' ' to finish): ")
    if user_input == '':
        break
    age = int(age_input)
    if age < 3:
        price = 0
        users.append(user_input)
    elif age in range(3,12):
        price=10 
        cost.append(price)
        users.append(user_input)
        total_cost=int(sum(cost))     
    elif age>13:
        price=15  
        cost.append(price)
        users.append(user_input)
        total_cost=int(sum(cost)) 
    print(users)
    print("your total ticket cost is", total_cost)
    if age in range(16,21): #create new list for users and total cost with age restrictions
        price=15
        new_users.append(user_input)
        new_cost.append(price)
        total_cost1=int(sum(new_cost))
    print(new_users)
    print("your total ticket cost is", total_cost1) 
#ex10 Sandwich orders
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwich=[]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
finished_sandwich = sandwich_orders
for item in finished_sandwich:
    print(f'I made your {item} sandwich')
print(finished_sandwich)    
 