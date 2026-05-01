class AttackAction:
    def __init__(self, name: str, damage: int, stamina_cost: int):
        self.name = name
        self.damage = damage
        self.stamina_cost = stamina_cost

    def execute(self, actor, target):
        if actor.stamina < self.stamina_cost:
            return f"{actor.name} tried to attack but has no stamina!"

        target.health -= self.damage
        target.health = max(target.health, 0)

        actor.stamina -= self.stamina_cost
        actor.stamina = max(actor.stamina, 0)

        return f"{actor.name} attacks {target.name} for {self.damage} damage!"