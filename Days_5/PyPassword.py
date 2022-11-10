#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'password_list', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_list = []
for i in range(0,nr_letters):
    password_list.append(letters[random.randint(0, len(letters) - 1)])
    
for i in range(1,nr_symbols+1):
    password_list.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(1,nr_numbers+1):
    password_list.append(numbers[random.randint(0, len(numbers) - 1)])  

print(password_list)
# Mezcla los elementos de la lista
random.shuffle(password_list)  

password = ""
for i in password_list:
    password += i
    
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# all = [letters, symbols, numbers]
# longitud = [nr_letters, nr_symbols, nr_numbers]
# longi = nr_numbers + nr_symbols + nr_letters
# password_list = ""

# for i in range(0, longi):
#     nro = random.randint(0,2)
#     while (longitud[nro] < 1):
#         nro = random.randint(0,2) 
#     longitud[nro] -= 1    
#     password_list += all[nro][random.randint(0,len(all[nro])-1)]     

# print(f"Your Password {password_list}\n")  


