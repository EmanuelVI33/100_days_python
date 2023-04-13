print('''
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \
   |             | )  )
   |             |/  /
   |             /  /    
   |            (  /
   \             y'
    `-.._____..-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direccion = input("Left or Right: ")

if (direccion=="left"):
    desicion = input("Swin or Wait: ")
    if (desicion=="wait"):
        door = input("Which Door? ")
        if (door=="yellow"):
            print("Your Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")