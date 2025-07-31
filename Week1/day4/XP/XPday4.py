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
basket.add("Kiwi")
basket.add("Apples")
basket.clear()
print(basket)

#ex4 Floats
my_list=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.]