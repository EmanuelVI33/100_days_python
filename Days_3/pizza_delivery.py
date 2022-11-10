

print("Welcome to Python Pizza Delivery")
size = input("What size pizza do you want? S, M o L: ")
add_peperoni = input("Do you want Peperoni? Y or N: ")
extra_chesse = input("Do you want extra cheese? Y or N: ")
price = 0

if (size == 'Y'):
    price += 15
    if(add_peperoni == 'Y'):
        price += 2    
else:
    if (add_peperoni == 'Y'):
        price += 3
    if(size == 'M'):
        price += 20
    else: 
        price += 25
        
if(extra_chesse == 'Y'):
    price += 1
        
print(f"Your final bill is: {price}")