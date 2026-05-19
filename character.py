
class Character:
    def __init__(self, name: str, health: int, stamina: int, actions: list):
        self.name = name
        self.health = health
        self.health_max = health
        self.stamina = stamina
        self.stamina_max = stamina
        self.actions = list(actions) if actions else [] # List of actions objects (e.g., AttackAction, HealAction)

        self.is_defending = False
    
    def take_damage(self, amount):
        if self.is_defending:
            amount = amount // 2
            self.is_defending = False
        self.health -= amount
        self.health = max(self.health, 0)
        

    def use_stamina(self, amount):
        self.stamina -= amount
        self.stamina = max(self.stamina, 0)

    def heal(self, amount):
        self.health += amount
        self.health = min(self.health, self.health_max)
    
    def recover_stamina(self, amount):
        self.stamina += amount
        self.stamina = min(self.stamina, self.stamina_max)

    def is_alive(self):
        return self.health > 0


    def get_action(self, index):
        if 0 <= index < len(self.actions):
            return self.actions[index]
        return None
