from character import Character
from action import AttackAction

hero = Character("Hero", 100, 50, [AttackAction("Slash", 10, 5)])
enemy = Character("Enemy", 80, 40, [AttackAction("Bite", 6, 4)])   

while True:
    hero_execute = hero.actions[0].execute(hero, enemy)
    print(hero_execute)
    enemy_execute = enemy.actions[0].execute(enemy, hero)
    print(enemy_execute)
    print(f"{hero.name} - Health: {hero.health}/{hero.health_max}, Stamina: {hero.stamina}/{hero.stamina_max}")
    print(f"{enemy.name} - Health: {enemy.health}/{enemy.health_max}, Stamina: {enemy.stamina}/{enemy.stamina_max}")
    print("-" * 30)
    if hero.health <= 0:
        print(f"{hero.name} has been defeated! {enemy.name} wins!")
        break
    elif enemy.health <= 0:
        print(f"{enemy.name} has been defeated! {hero.name} wins!")
        break