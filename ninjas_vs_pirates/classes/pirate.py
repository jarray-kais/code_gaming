import random

class Pirate:
    def __init__(self, name, point_of_view, attacks):
        self.name = name
        self.point_of_view = point_of_view
        self.attacks = attacks

    def attack(self, adversaire):
        degats = random.randint(0, self.attacks)
        adversaire.point_of_view -= degats
        print(f"{self.name} attack {adversaire.name} and inflicts {degats} points of damage.")

    def is_alive(self):
        return self.point_of_view > 0