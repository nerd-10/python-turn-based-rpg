class AttackAction:
    def __init__(self, name: str, damage: int, stamina_cost: int):
        self.name = name
        self.damage = damage
        self.stamina_cost = stamina_cost

    def execute(self, actor, target):
        if actor.stamina < self.stamina_cost:
            return(f"{actor.name} does not have enough stamina to perform {self.name}!")
            
        target.health -= self.damage
        target.health = max(target.health, 0)  # Ensure health doesn't go below 0

        actor.stamina -= self.stamina_cost  # Reduce actor's stamina
        actor.stamina = max(actor.stamina, 0)  # Ensure stamina doesn't go below 0
        
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")