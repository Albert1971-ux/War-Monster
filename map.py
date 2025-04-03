from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Axe(Weapon):
    def attack(self):
        return "рубит топором"


class MagicStaff(Weapon):
    def attack(self):
        return "кастует магический снаряд"


class Fighter:
    def __init__(self, name, weapon: Weapon = None):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает {new_weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
            return True
        else:
            print(f"{self.name} не имеет оружия!")
            return False


class Monster:
    def __init__(self, name, health=2):
        self.name = name
        self.health = health

    def is_defeated(self):
        return self.health <= 0

    def take_hit(self):
        self.health -= 1
        if self.is_defeated():
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} ранен, но еще в строю!")


def battle(fighter: Fighter, monster: Monster):
    print("\nНачинается бой!")
    while not monster.is_defeated():
        if fighter.attack():
            monster.take_hit()
        else:
            break


if __name__ == "__main__":
    #Создаём персонажей

    hero = Fighter("Боец")
    orc = Monster("Орк")

    hero.change_weapon(Sword())
    battle(hero, orc)

    # Новый монстр
    troll = Monster("Тролль", 3)

    hero.change_weapon(Bow())
    battle(hero, troll)

    # Добавляем новое оружие
    hero.change_weapon(Axe())
    battle(hero, Monster("Гоблин"))

    hero.change_weapon(MagicStaff())
    battle(hero, Monster("Дракон", 4))
