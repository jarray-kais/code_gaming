from classes.ninja import Ninja
from classes.pirate import Pirate

player1 = Ninja("ninja", 100, 20)
player2 = Pirate("pirate", 100, 18)

# Boucle de jeu
while player1.is_alive() and player1.is_alive():
    # Tour du joueur 1
    player1.attack(player2)
    
    # Vérifier si joueur 2 est toujours en vie
    if not player2.is_alive():
        print(f"{player2.name} is defeated!")
        break

    # Tour du joueur 2
    player2.attack(player1)

    # Vérifier si joueur 1 est toujours en vie
    if not player1.is_alive():
        print(f"{player1.name} is defeated!")

# Afficher le résultat du jeu
if player1.is_alive():
    print(f"{player1.name} win the victory!")
else:
    print(f"{player2.name} win the victory!")