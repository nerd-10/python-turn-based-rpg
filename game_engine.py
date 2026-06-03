from character import Character
import random

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
            print("R: Run away")
            try:
                choice = (input("Choose an action: "))
            except ValueError:
                print("Invalid input. Please enter a number corresponding to an action or R to run.")
                continue

            if choice.lower() == 'r':
                return False
            
            try:
                choice = int(choice)

            except ValueError:
                print("Invalid input. Please enter a number corresponding to an action or R to run.")
                continue

            action = (self.hero.get_action(choice))

            if action:
                result = action.execute(self.hero, self.enemy)
                print(result)
            else:
                print("Invalid action. Try again.")
                continue
            return True
        
    def enemy_turn(self):
        valid_actions = []
        for action in self.enemy.actions:
            if action.name == "Heal" and self.enemy.health == self.enemy.health_max:
                continue
            if action.name == "Rest" and self.enemy.stamina == self.enemy.stamina_max:
                continue
            valid_actions.append(action)
        enemy_action = random.choice(valid_actions) if valid_actions else None

        if enemy_action is None:
            print("Enemy has no valid action!")
            return

        result = enemy_action.execute(self.enemy, self.hero)
        print(result)


    def display_status(self):
        print(f"\n{self.hero.name} - Health: {self.hero.health}, Stamina: {self.hero.stamina}")
        print(f"{self.enemy.name} - Health: {self.enemy.health}, Stamina: {self.enemy.stamina}")


    def run(self):
        self.display_status()  
        while True:
                p_move = self.player_turn()
                if not p_move:
                    print("You chose to run away to main menu")
                    break
                if self.enemy.health <= 0:
                    print(f"{self.enemy.name} has been defeated! You win!")
                    break
                self.enemy_turn()
                if self.hero.health <= 0:
                    print(f"{self.hero.name} has been defeated! Game over!")
                    break
                self.display_status()