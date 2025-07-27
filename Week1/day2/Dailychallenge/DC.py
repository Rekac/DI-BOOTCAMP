# 1. Ask for user input
word=input("Enter a string: ")
print(len(word))
#print first and last character
#print(word[0,word[-1]])
#Loop
for i in range(1, len(word) + 1):
    print(word[:i])
#lengh of string 
b=len(word)
#validate string 
if len(word)<10:
    print("String not long enough.")
elif len(word)==10:
    print("Perfect string")
else:
    print("String too long.")