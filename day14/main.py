import datas as d
import random
import os # Para limpiar la consola

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
      """

# Verifica si contina jugando
def check(option: str):
    print(option_a["follower_count"], option_b["follower_count"])
    if option.upper() == "A":
        return option_a["follower_count"] >= option_b["follower_count"]
    else:
        return option_b["follower_count"] >= option_a["follower_count"]

# Muestra los datos en pantalla
def show(option_a, option_b):
    print(logo)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print("""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
    """)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")


# Longitud de la lista
longi = len(d.data)

score = 0

# seleccionar dos personas al azar
option_a = d.data[random.randint(1, longi - 1)]
option_b = d.data[random.randint(1, longi - 1)]

# Para que no elija la misma opcion
def different_person(longi, option_a, option_b):
    while option_a["name"] == option_b["name"]: 
        option_b = d.data[random.randint(1, longi - 1)]
    return option_b

option_b = different_person(longi, option_a, option_b)

show(option_a, option_b)

# Ingresar por teclado la opción
opt = "A" if input("Who has more followers? Type 'A' or 'B':") == "A" else "B"

# Verifica si continua jugando
option = check(opt)

while option:
    score += 1
    os.system('cls')
    # La opcion B pasa a ser la opcion A
    option_a = option_b
    option_b = different_person(longi, option_a, option_b)
    
    show(option_a, option_b)
    opt = "A" if input("Who has more followers? Type 'A' or 'B':") == "A" else "B"
    
    # Verificar
    option = check(opt)
    
# En algun momento debe perder y mostramos mensaje de error
print(f"Sorry, that's wrong. Final score: {score}")
    



