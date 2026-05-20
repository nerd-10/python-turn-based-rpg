from character import Character
import random

#next refactoring game engine by splitting the main game loop into separate methods for player and enemy turns, and adding a method to display status after each turn
class GameEngine:
    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def player_turn(self):
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
            break
    def enemy_turn(self):
        enemy_action = random.choice(self.enemy.actions) if self.enemy.actions else None

        if enemy_action is None:
            print("Enemy has no valid action!")
            return

        result = enemy_action.execute(self.enemy, self.hero)
        print(result)


    def display_status(self):
        print(f"\n{self.hero.name} - Health: {self.hero.health}, Stamina: {self.hero.stamina}")
        print(f"{self.enemy.name} - Health: {self.enemy.health}, Stamina: {self.enemy.stamina}")


    def run(self):
        while True:
                self.player_turn()
                if self.enemy.health <= 0:
                    print(f"{self.enemy.name} has been defeated! You win!")
                    break
                self.enemy_turn()
                if self.hero.health <= 0:
                    print(f"{self.hero.name} has been defeated! Game over!")
                    break
                self.display_status()