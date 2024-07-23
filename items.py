"""
Módulo `items`

Este módulo define as classes e dados relacionados aos itens no jogo.

Classes:
- `ItemType`: Enum que define os tipos de itens disponíveis: Arma, Poção e Escudo.
- `Item`: Classe base para todos os itens, com propriedades e métodos comuns.
- `Weapon`: Classe derivada de `Item` que representa armas e suas propriedades específicas.
- `Potion`: Classe derivada de `Item` que representa poções e suas propriedades específicas.
- `Shield`: Classe derivada de `Item` que representa escudos e suas propriedades específicas.

Dados:
- `weapons`: Lista de armas disponíveis no jogo, contendo nome, valor e dano.
- `shields`: Lista de escudos disponíveis no jogo, contendo nome, valor e bloqueio.
- `potions`: Lista de poções disponíveis no jogo, contendo nome, valor e quantidade de cura.
- `weight`: Lista de pesos para cada tipo de item, indicando a probabilidade relativa de encontrar cada tipo.

Dependências:
- `enum`: Para a definição da classe `ItemType`.

Métodos das Classes:
- `Item`:
  - `__init__(self, name, value, item_type, level=1)`: Inicializa um item com nome, valor, tipo e nível.
  - `__str__(self)`: Retorna uma representação em string do item.
  - `upgrade(self)`: Atualiza o nível do item e aumenta seu valor.

- `Weapon` (herda de `Item`):
  - `__init__(self, name, value, damage, level=1)`: Inicializa uma arma com dano.
  - `__str__(self)`: Retorna uma representação em string da arma.
  - `upgrade(self)`: Atualiza a arma, aumentando o dano.
  - `calculate_next_damage(self)`: Calcula o dano da próxima atualização.

- `Potion` (herda de `Item`):
  - `__init__(self, name, value, heal_amount, level=1)`: Inicializa uma poção com capacidade de cura.
  - `__str__(self)`: Retorna uma representação em string da poção.
  - `upgrade(self)`: Atualiza a poção, aumentando a cura.
  - `calculate_next_heal(self)`: Calcula a cura da próxima atualização.

- `Shield` (herda de `Item`):
  - `__init__(self, name, value, block_amount, level=1)`: Inicializa um escudo com capacidade de bloqueio.
  - `__str__(self)`: Retorna uma representação em string do escudo.
  - `upgrade(self)`: Atualiza o escudo, aumentando o bloqueio.
  - `calculate_next_block(self)`: Calcula o bloqueio da próxima atualização.
"""

from enum import Enum

class ItemType(Enum):
    """
    Enum para representar os diferentes tipos de itens no jogo.

    Atributos:
    WEAPON (str): Representa um item do tipo arma.
    POTION (str): Representa um item do tipo poção.
    SHIELD (str): Representa um item do tipo escudo.
    """
    WEAPON = "Weapon"
    POTION = "Potion"
    SHIELD = "Shield"

class Item:
    """
    Representa um item genérico no jogo.

    Atributos:
    name (str): O nome do item.
    value (float): O valor do item em moeda.
    item_type (ItemType): O tipo de item (arma, poção ou escudo).
    level (int): O nível do item (padrão é 1).

    Métodos:
    __str__(): Retorna uma representação em string do item.
    upgrade(): Atualiza o nível do item e aumenta seu valor.
    """
    def __init__(self, name, value, item_type, level=1):
        """
        Inicializa as propriedades do item.

        Parâmetros:
        name (str): O nome do item.
        value (float): O valor do item.
        item_type (ItemType): O tipo de item.
        level (int, opcional): O nível inicial do item. Padrão é 1.
        """
        self.name = name  # Nome do item
        self.value = value  # Valor do item
        self.item_type = item_type  # Tipo do item (arma, poção, escudo)
        self.level = level  # Nível do item

    def __str__(self):
        """
        Retorna uma representação em string do item.

        Retorna:
        str: A string representando o item, incluindo nome, valor, nível e tipo.
        """
        return f"{self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Tipo: {self.item_type.value})"

    def upgrade(self):
        """
        Atualiza o nível do item e aumenta seu valor.

        O valor do item aumenta em 50% a cada upgrade.
        """
        self.level += 1
        self.value *= 1.5  # Valor aumenta em 50% a cada upgrade

class Weapon(Item):
    """
    Representa uma arma no jogo.

    Atributos:
    name (str): O nome da arma.
    value (float): O valor da arma em moeda.
    damage (float): O dano causado pela arma.
    level (int): O nível da arma (padrão é 1).

    Métodos:
    __str__(): Retorna uma representação em string da arma.
    upgrade(): Atualiza a arma, aumentando o dano.
    calculate_next_damage(): Calcula o dano da próxima atualização.
    """
    def __init__(self, name, value, damage, level=1):
        """
        Inicializa uma arma com dano.

        Parâmetros:
        name (str): O nome da arma.
        value (float): O valor da arma.
        damage (float): O dano causado pela arma.
        level (int, opcional): O nível inicial da arma. Padrão é 1.
        """
        super().__init__(name, value, ItemType.WEAPON, level)
        self.damage = damage  # Dano causado pela arma

    def __str__(self):
        """
        Retorna uma representação em string da arma.

        Retorna:
        str: A string representando a arma, incluindo nome, valor, nível e dano.
        """
        return f"{self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Dano: {self.damage:.2f})"

    def upgrade(self):
        """
        Atualiza a arma, aumentando o dano.

        O dano aumenta em 30% a cada upgrade.
        """
        super().upgrade()
        self.damage *= 1.3  # Dano aumenta em 30% a cada upgrade

    def calculate_next_damage(self):
        """
        Calcula o dano da próxima atualização.

        Retorna:
        float: O dano estimado da próxima atualização.
        """
        return self.damage * 1.3

class Potion(Item):
    """
    Representa uma poção no jogo.

    Atributos:
    name (str): O nome da poção.
    value (float): O valor da poção em moeda.
    heal_amount (float): A quantidade de cura fornecida pela poção.
    level (int): O nível da poção (padrão é 1).

    Métodos:
    __str__(): Retorna uma representação em string da poção.
    upgrade(): Atualiza a poção, aumentando a cura.
    calculate_next_heal(): Calcula a cura da próxima atualização.
    """
    def __init__(self, name, value, heal_amount, level=1):
        """
        Inicializa uma poção com capacidade de cura.

        Parâmetros:
        name (str): O nome da poção.
        value (float): O valor da poção.
        heal_amount (float): A quantidade de cura fornecida pela poção.
        level (int, opcional): O nível inicial da poção. Padrão é 1.
        """
        super().__init__(name, value, ItemType.POTION, level)
        self.heal_amount = heal_amount  # Quantidade de cura da poção

    def __str__(self):
        """
        Retorna uma representação em string da poção.

        Retorna:
        str: A string representando a poção, incluindo nome, valor, nível e cura.
        """
        return f"Poção: {self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Cura: {self.heal_amount:.2f})"

    def upgrade(self):
        """
        Atualiza a poção, aumentando a cura.

        A cura aumenta em 15% a cada upgrade.
        """
        super().upgrade()
        self.heal_amount *= 1.15  # Cura aumenta em 15% a cada upgrade

    def calculate_next_heal(self):
        """
        Calcula a cura da próxima atualização.

        Retorna:
        float: A cura estimada da próxima atualização.
        """
        return self.heal_amount * 1.15

class Shield(Item):
    """
    Representa um escudo no jogo.

    Atributos:
    name (str): O nome do escudo.
    value (float): O valor do escudo em moeda.
    block_amount (float): A quantidade de bloqueio fornecida pelo escudo.
    level (int): O nível do escudo (padrão é 1).

    Métodos:
    __str__(): Retorna uma representação em string do escudo.
    upgrade(): Atualiza o escudo, aumentando o bloqueio.
    calculate_next_block(): Calcula o bloqueio da próxima atualização.
    """
    def __init__(self, name, value, block_amount, level=1):
        """
        Inicializa um escudo com capacidade de bloqueio.

        Parâmetros:
        name (str): O nome do escudo.
        value (float): O valor do escudo.
        block_amount (float): A quantidade de bloqueio fornecida pelo escudo.
        level (int, opcional): O nível inicial do escudo. Padrão é 1.
        """
        super().__init__(name, value, ItemType.SHIELD, level)
        self.block_amount = block_amount  # Quantidade de bloqueio do escudo

    def __str__(self):
        """
        Retorna uma representação em string do escudo.

        Retorna:
        str: A string representando o escudo, incluindo nome, valor, nível e bloqueio.
        """
        return f"{self.name} (Valor: R${self.value:.2f}, Nível: {self.level}, Bloqueio: {self.block_amount:.2f})"

    def upgrade(self):
        """
        Atualiza o escudo, aumentando o bloqueio.

        O bloqueio aumenta em 20% a cada upgrade.
        """
        super().upgrade()
        self.block_amount *= 1.2  # Bloqueio aumenta em 20% a cada upgrade

    def calculate_next_block(self):
        """
        Calcula o bloqueio da próxima atualização.

        Retorna:
        float: O bloqueio estimado da próxima atualização.
        """
        return self.block_amount * 1.2

# Lista de espadas com nome, valor e dano
weapons = [
    ("Espada de Treinamento", 50, 12),
    ("Espada do Guerreiro", 100, 20),
    ("Lâmina da Tempestade", 200, 35)
]

# Lista de escudos com nome, valor e bloqueio
shields = [
    ("Escudo de Madeira", 30, 5),
    ("Escudo de Ferro", 70, 8),
    ("Escudo de Aço", 150, 15)
]

# Lista de poções com nome, valor e quantidade de cura
potions = [
    ("Poção de Cura Leve", 20, 20),
    ("Poção de Cura Média", 50, 30),
    ("Poção de Cura Forte", 100, 40)
]

# Pesos para itens, indicando probabilidade relativa de encontrar cada tipo de item
weight = [0.6, 0.3, 0.1]
