import random

class Enemy:
    def __init__(self, name, hp, taunt):
        self.name = name
        self.hp = hp
        self.taunt_message = taunt

    def lose_hp(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        damage = random.randint(1, 20)
        player.lose_hp(damage)
        print(f"💢 {self.name} attacked you for {damage} damage! 😱 You better SLAY BACK! 💅")
        
    def taunt(self):
        print(f"😏 {self.taunt_message}")
