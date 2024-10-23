from player import Player
from enemy import Enemy
import random

def start_battle(player, enemy):
    print(f"👹 OH NO, {enemy.name} just popped outta nowhere! Time to SLAY or CLICK, queen! 💅")
    enemy.taunt()

    while player.is_alive() and enemy.is_alive():
        print(f"\n✨ Your HP: {player.hp}")
        print(f"💀 {enemy.name}'s HP: {enemy.hp}")
        choice = input("Press [S] to SLAY (10 HP) 🗡️ or [C] to CLICK (15 HP) 💥: ").lower()

        if choice == "s":
            player.slay(enemy)
        elif choice == "c":
            player.click(enemy)
        else:
            print("Umm, we only SLAY or CLICK here, hun. Try again. 💅")

        if enemy.is_alive():
            enemy.attack(player)

def game():
    print("""
    💅💬 [BESTIE]: O-M-G, gurl, guess what? The SLAY ZONE is like, so totally real! You’re gonna need to like, 
    fight ALL the fake haters, denial queens, and Drama Llamas out there. It’s like, you or them, babe! 
    So sharpen that eyeliner and get ready to throw SHADE.

    🌈💬 [YOU]: OMG stop, bestie. Are you serious right now? 💀 Like, what do I do? Do I call my therapist or what?! 
    This is too much! I’m not emotionally prepared for this kind of drama. 😱

    💅💬 [BESTIE]: GURL, listen, this is the ONLY way to keep your crown. 👑✨ You either SLAY or let them drag 
    you down with their messy energy. It's called survival of the fiercest. 
    Now are you gonna fight or let Karen talk to your manager?! 🎤🔥

    🌈💬 [YOU]: Okay, okay, FINE. I will protect my crown! No hater or fake friend is gonna come for me! 
    Let's get this started! Time to SNATCH some wigs. 💁‍♀️💥
    """)

    print("✨ Welcome to the SLAY ZONE ✨")
    print("You’re about to enter a world where the shade is real, the memes are legendary, and only the fiercest survive. 💅")
    player_name = input("What’s your name, superstar? ")
    player = Player(player_name, 100)

    enemies = [
        Enemy("Shady Diva 👁️👄👁️", 30, "Honey, denial isn't just a river in Egypt, it's your whole life! 🌊💅"),
        Enemy("Lucifer 🔥😈", 25, "Your man ain't straight, sis. He’s busy dancing with rainbows! 🌈💀"),
        Enemy("Karen 👩‍🦳💼", 35, "Excuse me, can I speak to the manager? 😤☕"),
        Enemy("Salty Icon 🧂👑", 40, "Not me being dramatic, YOU’RE the one crying, sis. 😭🎭"),
        Enemy("Petty Queen 🐸☕", 20, "You thought pumpkin spice was a personality trait? 🚫🎃")
    ]

    while player.is_alive() and enemies:
        enemy = random.choice(enemies)
        start_battle(player, enemy)

        if not player.is_alive():
            print("\n💔 Oh no! You lost your crown... but listen, queen: 'We don’t need no negativity in our timeline.' You’ll rise again! 🌈✨")
        else:
            print(f"Mood: {player.name} walking away with the crown like 'I woke up like this.' 💁‍♀️✨")
            enemies.remove(enemy)

        if not enemies:
            print(f"🎉 OMGGGG {player_name}, YOU SLAYED ALL THE HATERS!! 👑✨")
            print("\n👑 Congratulations, ICON! You slayed every one of those frenemies. The internet is now making 'legend' memes in your honor. 💅🔥")
            break

if __name__ == "__main__":
    game()
