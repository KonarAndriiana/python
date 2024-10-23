from enemy import Enemy
import random

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def lose_hp(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def slay(self, enemy):
        damage = 10
        enemy.lose_hp(damage)
        print(f"⚔️ SLAYED {enemy.name} for {damage} HP! 🥵✨ You’re a whole mood! #QueenEnergy")

    def click(self, enemy):
        damage = 15
        enemy.lose_hp(damage)
        print(f"💥 CLICKED {enemy.name} for {damage} HP! 💣💥 That was personal! #YASSS")
