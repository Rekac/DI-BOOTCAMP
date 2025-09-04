import random
def random_number(num1,num2):
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    if num1==num2:
        print(f"great! both numbers are the same")
    else:
        print(f"Sorry! {num1} is not the same as {num2}") 
random_number(num1=1,num2=100)
