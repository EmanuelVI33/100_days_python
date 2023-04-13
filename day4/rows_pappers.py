import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista = [rock, paper, scissors]
user = random.randint(0,2)
computer = random.randint(0,2)

print(lista[user]+"\n")
print(f"Computer: \n{lista[computer]}")

if (user == computer):
    print("Empate")
elif(user == 0 and (computer != 1 or computer == 2)): # Rock
    print("Your Win")
elif(user == 1 and (computer != 2 or computer == 0)): # Paper
    print("Your Win")    
elif(user == 2 and (computer != 0 or computer == 1)): # scissors
    print("Your Win")      
else: 
    print("Your Loose")