from enum import Enum

class ItemType(Enum):
    WEAPON = "Weapon"
    POTION = "Potion"
    SHIELD = "Shield"

class Item:
    def __init__(self, name, value, item_type, level=1):
        self.name = name
        self.value = value
        self.item_type = item_type
        self.level = level

    def __str__(self):
        return f"{self.name} (Valor: ${self.value}, Nível: {self.level}, Tipo: {self.item_type.value})"

    def upgrade(self):
        self.level += 1
        self.value += 10

class Weapon(Item):
    def __init__(self, name, value, damage, level=1):
        super().__init__(name, value, ItemType.WEAPON, level)
        self.damage = damage

    def __str__(self):
        return f"Espada: {self.name} (Valor: ${self.value}, Nível: {self.level}, Dano: {self.damage})"

    def upgrade(self):
        super().upgrade()
        self.damage += 5

class Potion(Item):
    def __init__(self, name, value, heal_amount, level=1):
        super().__init__(name, value, ItemType.POTION, level)
        self.heal_amount = heal_amount

    def __str__(self):
        return f"Poção: {self.name} (Valor: ${self.value}, Nível: {self.level}, Cura: {self.heal_amount})"

    def upgrade(self):
        super().upgrade()
        self.heal_amount += 10

class Shield(Item):
    def __init__(self, name, value, block_amount, level=1):
        super().__init__(name, value, ItemType.SHIELD, level)
        self.block_amount = block_amount

    def __str__(self):
        return f"Escudo: {self.name} (Valor: ${self.value}, Nível: {self.level}, Bloqueio: {self.block_amount})"

    def upgrade(self):
        super().upgrade()
        self.block_amount += 3
