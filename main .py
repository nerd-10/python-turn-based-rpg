from character import Character
from action import AttackAction
from action import HealAction
from game_engine import GameEngine

hero = Character("Hero", 100, 50, [AttackAction("Slash", 10, 5), HealAction("Heal", 20, 10)])
enemy = Character("Enemy", 80, 40, [AttackAction("Bite", 6, 4), HealAction("Heal", 15, 8)])

engine = GameEngine(hero, enemy)
engine.run()    