from character import Character
from action import AttackAction
from action import HealAction
import random

class GameEngine:
    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def run(self):
        while True:
            # --- PLAYER TURN ---
            print(f"\n{self.hero.name}'s turn:")
            for i, action in enumerate(self.hero.actions):
                print(f"{i}: {action.name} ({action.get_details()})")
            try:
                choice = int(input("Choose an action: "))
            except ValueError:
                print("Invalid input! Enter a number.")
                continue

            action = self.hero.get_action(choice)

            if action:
                result = action.execute(self.hero, self.enemy)
                print(result)
            else:
                print("Invalid action. Try again.")
                continue

            if self.enemy.health <= 0:
                print(f"{self.enemy.name} has been defeated! You win!")
                break

            # --- ENEMY TURN ---
            print("\nEnemy Turn:")
            enemy_action = random.choice(self.enemy.actions) if self.enemy.actions else None

            if enemy_action is None:
                print("Enemy has no valid action!")
                return

            result = enemy_action.execute(self.enemy, self.hero)
            print(result)

            if self.hero.health <= 0:
                print(f"{self.hero.name} has been defeated! Game Over!")
                break

            # --- STATUS ---
            print(f"\nStatus:")
            print(f"{self.hero.name}: {self.hero.health}/{self.hero.health_max} HP | {self.hero.stamina}/{self.hero.stamina_max} ST")
            print(f"{self.enemy.name}: {self.enemy.health}/{self.enemy.health_max} HP | {self.enemy.stamina}/{self.enemy.stamina_max} ST")