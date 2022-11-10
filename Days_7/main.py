import random
import hagman
import list_words

word_list = list_words.word_list

chosen_word = random.choice(word_list)

display = []
longitud = len(chosen_word) #  Emanuel
for _ in range(longitud): # No usamos i _
    display += "_"

print(hagman.logo)
print(chosen_word)
wins = 0
copiaWins = wins
left = 6

while (wins < longitud and left > 0): 
    guess = input("Guess a letter: ").lower()   
    copiaWins = wins
    for i in range(longitud):
        if (chosen_word[i] == guess): 
            if (display[i] == guess):
                print("Ya adivinaste esta palabra")
                break
            display[i] = guess
            wins += 1

    if (copiaWins == wins and display[i] != guess):
        print("No existe la letra, pierdes una vida")
        left -= 1
            
    print(f"{' '.join(display)}")  
    print(hagman.stages[left])
    
if (wins == longitud): 
    print("You Win")
else:
    print("You Loose")