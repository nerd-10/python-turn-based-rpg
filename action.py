#base class for actions that characters can perform in the game
class Action:
    def __init__(self, name: str, stamina_cost: int):
        self.name = name
        self.stamina_cost = stamina_cost
    
    def can_execute(self, actor):
        return actor.stamina >= self.stamina_cost
    
    def execute(self, actor, target):
        raise NotImplementedError("Execute method must be implemented by subclasses")
    def get_details(self):
        return (f"(Cost: {self.stamina_cost} ST)")
    

#class to execute an attack action, which reduces the target's health and consumes the actor's stamina
class AttackAction(Action):
    def __init__(self, name: str, damage: int, stamina_cost: int):
        super().__init__(name, stamina_cost)
        self.damage = damage

    def execute(self, actor, target):
        if not self.can_execute(actor):
            return f"{actor.name} tried to attack but has no stamina!"
        
        target.take_damage(self.damage)
        actor.use_stamina(self.stamina_cost)

        return f"{actor.name} attacks {target.name} for {self.damage} damage!"
    
    def get_details(self):
        return (f"(Damage: {self.damage}, Cost: {self.stamina_cost} ST)")
    
#class to execute a jheal action, which restores the actor's health and consumes stamina
class HealAction(Action):
    def __init__(self, name: str, heal_amount: int, stamina_cost: int):
        super().__init__(name, stamina_cost)
        self.heal_amount = heal_amount

    def execute(self, actor, target=None):
        if not self.can_execute(actor):
            return f"{actor.name} tried to heal but has no stamina!"
        
        actor.heal(self.heal_amount)
        actor.use_stamina(self.stamina_cost)

        return f"{actor.name} heals for {self.heal_amount} health!"
    
    def get_details(self):
        return (f"(Heal: {self.heal_amount}, Cost: {self.stamina_cost} ST)")
    

#class to execute a defend action, which reduces incoming damage for the next turn and consumes stamina
class DefendAction(Action):
    def __init__(self, name: str, stamina_cost: int):
        super().__init__(name, stamina_cost)

    def execute(self, actor, target=None):
        if not self.can_execute(actor):
            return f"{actor.name} tried to defend but has no stamina!"
        
        actor.is_defending = True
        actor.use_stamina(self.stamina_cost)

        return f"{actor.name} raises their shield to defend!"
    
    def get_details(self):
        return (f"(Cost: {self.stamina_cost} ST)")