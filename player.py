from items import Weapon, Shield, Potion

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.exp = 0
        self.inventory = []
        self.money = 0
        self.weapon = None
        self.shield = None

    def show_status(self):
        print(f"{self.name}'s HP: {self.hp}")
        print("Equipamentos:")
        if self.weapon:
            print(f"  - Arma: {self.weapon}")
        else:
            print("  - Arma: Nenhuma")
        if self.shield:
            print(f"  - Escudo: {self.shield}")
        else:
            print("  - Escudo: Nenhum")
        print("Inventário:")
        if self.inventory:
            for index, item in enumerate(self.inventory, start=1):
                print(f"  [{index}] - {item}")
        else:
            print("  Nenhum item no inventário.")
        print(f"Dinheiro: ${self.money}")

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item não encontrado no inventário.")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def earn_money(self, value):
        self.money += value

    def is_alive(self):
        return self.hp > 0

    def equip_item(self, item_index):
        if 0 <= item_index < len(self.inventory):
            item_to_equip = self.inventory[item_index]
            if isinstance(item_to_equip, Weapon):
                self.weapon = item_to_equip
            elif isinstance(item_to_equip, Shield):
                self.shield = item_to_equip
            else:
                print("Este item não pode ser equipado.")
        else:
            print("Índice do item não encontrado no inventário.")
