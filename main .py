from character import Character
from action import AttackAction
from action import HealAction
from action import DefendAction
from action import StaminaRecoveryAction
from game_engine import GameEngine

hero = Character("Hero", 100, 50, [AttackAction("Slash", 10, 5), HealAction("Heal", 20, 10), DefendAction("Defend", 5), StaminaRecoveryAction("Rest",8)])
enemy = Character("Enemy", 80, 40, [AttackAction("Bite", 6, 4), HealAction("Heal", 15, 8), DefendAction("Defend", 4), StaminaRecoveryAction("Rest",6)])

engine = GameEngine(hero, enemy)
while True:
    print("Menu:")
    print("1: Start Game")
    print("2: Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        engine.run()
        break
    elif choice == '2':
        print("Exiting game. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter 1 to start the game or 2 to exit.")
    engine.run()    