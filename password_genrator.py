
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
 "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
 "Y", "Z" ]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
symbols = ["!", "@", "#", "$", "%", "%", "^", "&", "*", "+", "(", ")" ]

print("---------WELCOME TO PYPASSWORD GENERATOR-------")
new_letters = int(input("HOW MANY LETTERS WOULD YOU LIKE IN YOU PASSWORD?"))
new_numbers = int(input("HOW MANY NUMBERS WOULD YOU LIKE IN YOUR PASSWORD?"))
new_symbols = int(input("HOW MANY SYMBOLS WOULD YOU LIKEE IN YOUR PASSWORD?"))

#LEVEL1(easy)
password = ""
for char in range(1,new_letters + 1):
    password += random.choice(letters)

for char in range(1,new_numbers + 1):
    password += random.choice(numbers)     

for char in range(1,new_symbols + 1):
    password += random.choice(symbols)   

print(password)        

#level2(hard)
password_list = []
for char in range(1,new_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1,new_numbers + 1):
    password_list.append(random.choice(numbers))  

for char in range(1,new_symbols + 1):
    password_list.append(random.choice(symbols))   

print(password_list)        
random.shuffle(password_list)
print(password_list)

#password = ""
#for char in password_list:
 #   password
print(f"Your password is : {password}")

