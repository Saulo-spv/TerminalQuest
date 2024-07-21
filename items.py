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
        return f"{self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Tipo: {self.item_type.value})"

    def upgrade(self):
        self.level += 1
        self.value *= 1.5

class Weapon(Item):
    def __init__(self, name, value, damage, level=1):
        super().__init__(name, value, ItemType.WEAPON, level)
        self.damage = damage

    def __str__(self):
        return f"Espada: {self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Dano: {self.damage:.2f})"

    def upgrade(self):
        super().upgrade()
        self.damage *= 1.3

    def calculate_next_damage(self):
        return self.damage * 1.3

class Potion(Item):
    def __init__(self, name, value, heal_amount, level=1):
        super().__init__(name, value, ItemType.POTION, level)
        self.heal_amount = heal_amount

    def __str__(self):
        return f"Poção: {self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Cura: {self.heal_amount:.2f})"

    def upgrade(self):
        super().upgrade()
        self.heal_amount *= 1.15

    def calculate_next_heal(self):
        return self.heal_amount * 1.15

class Shield(Item):
    def __init__(self, name, value, block_amount, level=1):
        super().__init__(name, value, ItemType.SHIELD, level)
        self.block_amount = block_amount

    def __str__(self):
        return f"Escudo: {self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Bloqueio: {self.block_amount:.2f})"

    def upgrade(self):
        super().upgrade()
        self.block_amount *= 1.2

    def calculate_next_block(self):
        return self.block_amount * 1.2

# Lista de espadas
weapons = [
    Weapon("Espada de Treinamento", 50, 25),
    Weapon("Espada do Guerreiro", 100, 40),
    Weapon("Lâmina da Tempestade", 200, 60)
]

# Lista de escudos
shields = [
    Shield("Escudo de Madeira", 30, 10),
    Shield("Escudo de Ferro", 70, 20),
    Shield("Escudo de Aço", 150, 30)
]

# Lista de poções
potions = [
    Potion("Poção de Cura Leve", 20, 20),
    Potion("Poção de Cura Média", 50, 40),
    Potion("Poção de Cura Forte", 100, 60)
]

weight = [0.6, 0.3, 0.1]
