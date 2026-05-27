from character import Character
import random

#next enemy turn choice filtering for example if health is full or stamina is full then no healing actions or stamina recovery etc.
#no exit command for now, just ctrl+c to exit the game, maybe add a menu later with options to start a new game, exit, etc.
#pyageme then godot engine for graphics and animations for release, but for now just a text-based game to test the mechanics and balance of the game.

class GameEngine:
    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def player_turn(self):
        while True:
            print(f"\n{self.hero.name}'s turn:")
            for i, action in enumerate(self.hero.actions):
                print(f"{i}: {action.name} ({action.get_details()})")
            try:
                choice = (input("Choose an action: "))
                choice = int(choice)
                if choice.lower() == 'q':
                    print("Exiting game. Goodbye!")
                    exit()
            except ValueError:
                print("Invalid input. Please enter a number corresponding to an action or Q to quit.")
                continue

            action = (self.hero.get_action(choice))

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