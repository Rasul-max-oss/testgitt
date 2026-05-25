import random
import time

class Character:
    def __init__(self,name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        self.skills = []
        
    def attack(self, target):
        print(f"{self.name} атакует {target.name} ")
        self.energy -= 10
        
    def move(self):
        print(f"{self.name} ходит ")
    
    def get_hp(self):
        print(f"Здоровье {self.name} осталось {self.health} /100")


class Warrior(Character):
    def __init__(self,name, health, energy):
         super().__init__(name,health,energy)
         self.damage = 15
    
    
    def attack(self, target):
        print(f"{self.name} бьет мечом {target.name} ")
        target.health -= random.randint(0,100)
        self.energy -= 10
        

class Enemy(Character):
    def attack(self, target):
        print(f"{self.name} атакует {target.name} ")
        target.health -= random.randint(0,100)
        
        

class Mag(Character):
    def __init__(self,name, health, energy):
         super().__init__(name,health,energy)
         self.damage = 15
         self.fire = 40 # урон от заклинания огня
         self.water = 20 # урон от заклинания воды
         self.mana = 100
    
    def attack(self, target):
        print(f"{self.name} говорит заклинание огня и аттакует {target.name} ")
        target.health -= self.fire
        self.mana -= self.fire 
        
    def attack_water(self, target):
        print(f"{self.name} говорит заклинание воды и аттакует {target.name} ")
        target.health -= self.water
        self.mana -= self.water 



enemy1 = Enemy("Огр", 100, 100)
warrior1 = Warrior("Воин Петя", 100, 100)
mag = Mag("Маг Арсений",100,100)



print("Выберите героя: ")
print("1.Воин Петя")
print("2.Маг Арсений")
hero = input("За кого хотите играть: ")

while True:
    print("1.Ходить")
    print("2.Посмотреть здоровье")
    print("3.Битва с врагом")
    choice = input("Выберите действие: ")
    if choice == "3":
        if hero == "1":
            warrior1.attack(enemy1)
            enemy1.get_hp()
            time.sleep(3)
            enemy1.attack(warrior1)
            warrior1.get_hp()
            
        if hero == "2":
            mag.attack(enemy1)
            enemy1.get_hp()
            time.sleep(3)
            enemy1.attack(mag)
            mag.get_hp()