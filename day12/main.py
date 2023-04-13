# Variables globales y locales
enemies = 1


def increase_enemies() -> None:
    enemies = 2
    print(enemies)


increase_enemies()  # Imprime su variable local
print(enemies)  # Variable global imprime 1


def drink_potion():
    position_strength = 2
    print(position_strength)

drink_potion()
# print(position_strength)  it's local variable, scope is in drink_position

# Global Scope
person = 10


def count_person():
    p = 1
    print(person)   # global scope


# Block Scope
# Se pueden crear o no variables de acuerdo a la logica de nuestro programa
# sin necesidad de declarar previamente

# if 3 > 2:
#     a_variable = 10  # Cumple es una variable global
#
# print(a_variable)

game_level = 4
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]   # Variable local, alcance dentro de create_enemy()
    print(new_enemy)

create_enemy()


enemies = 1


def increase_enemies() -> None:
    global enemies
    enemies += 1     # Recomendable no modificar dentro de una funcion de local scope, una variable global
    print(enemies)

def increase_enemies2() -> None:
    return enemies + 1

increase_enemies()
enemies = increase_enemies2()
print(enemies)

# Global const
# Es mas usado en constante, cuando necesitamos acceder a esos valores
PI = 3.1416
URL = "emanuel.com"
YOUTUBE_LINK = "course.com"   # Conveción de constante

def show_link():

