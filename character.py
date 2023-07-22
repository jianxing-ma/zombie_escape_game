class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self, target):
        target.take_damage(self.attack)
        print(f"{self.name} attacks {target.name} and deals {self.attack} damage.")

    def take_damage(self, damage):
        self.health -= damage


class Player(Character):
    def __init__(self, name, health, attack, potion=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.potion = potion

    def evade(self, target):
        self.health -= target.attack // 10

    def collect_item(self, item):
        if item.__class__.__name__ == "Potion":
            self.potion += 1
            print("You got a potion!")
        elif item.__class__.__name__ == "Weapon":
            print(f"You got a {item.name}, attack +{item.value}")

    def heal(self):
        if self.potion > 0:
            self.health += 5
            self.potion -= 1
        else:
            print("No more potion left!")


class Zombie(Character):
    pass
