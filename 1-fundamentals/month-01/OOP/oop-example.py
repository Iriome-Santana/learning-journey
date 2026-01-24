

class Ninja:
    def __init__(self, name, hp, physic_attack, special_attack):
        self.name = name
        self.hp = hp
        self.physic_attack = physic_attack
        self.special_attack = special_attack
        
    def attack_enemy(self, enemy):
        enemy.hp -= self.physic_attack
        print(f"{self.name} attacks {enemy.name} for {self.physic_attack} damage")
        print(f"{enemy.name} has {enemy.hp} hp left")
        
    def show(self):
        print(self.name, self.hp, self.physic_attack, self.special_attack)
        
    def special_attack_enemy(self, enemy):
        enemy.hp -= self.special_attack
        print(f"{self.name} attacks {enemy.name} for {self.special_attack} damage")
        print(f"{enemy.name} has {enemy.hp} hp left")
        

naruto = Ninja("Naruto", 100, 10, 40)
sasuke = Ninja("Sasuke", 100, 20, 30)

naruto.show()
sasuke.show()
naruto.attack_enemy(sasuke)
naruto.show()
sasuke.show()
sasuke.special_attack_enemy(naruto)
naruto.show()
sasuke.show()

