import random
# Desde indice 0 a n
# Existe indice negativos, empieza a contrar desde el final
name_string = input("Give me everybody names, separated by a coma. ")
names = name_string.split(", ")
longitud = len(names) - 1
choosen = names[random.randint(0, longitud)] 

print(f"Paga {choosen}")