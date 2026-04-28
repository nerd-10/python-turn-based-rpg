from action import AttackAction

class Character:
    def __init__(self, name: str, health: int, stamina: int, actions: list):
        self.name = name
        self.health = health
        self.health_max = health
        self.stamina = stamina
        self.stamina_max = stamina
        self.actions = list(actions) if actions else [] # List of actions objects (e.g., AttackAction)

    def __get_action(self, index):
        if 0 <= index < len(self.actions):
            return self.actions[index]
        return None

hero = Character("Hero", 100, 50, [AttackAction("Slash", 10, 5)])
enemy = Character("Enemy", 80, 40, [AttackAction("Bite", 6, 4)])    