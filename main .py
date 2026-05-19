from character import Character
from action import AttackAction
from action import HealAction
from action import DefendAction
from action import StaminaRecoveryAction
from game_engine import GameEngine

hero = Character("Hero", 100, 50, [AttackAction("Slash", 10, 5), HealAction("Heal", 20, 10), DefendAction("Defend", 5), StaminaRecoveryAction("Rest",8)])
enemy = Character("Enemy", 80, 40, [AttackAction("Bite", 6, 4), HealAction("Heal", 15, 8), DefendAction("Defend", 4), StaminaRecoveryAction("Rest",6)])

engine = GameEngine(hero, enemy)
engine.run()    