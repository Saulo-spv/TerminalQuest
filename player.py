"""
Módulo `player`

Este módulo define a classe `Player` e suas funcionalidades para gerenciar o estado e as ações do jogador no jogo.

Classes:
- `Player`: Representa um jogador no jogo, gerenciando saúde, itens equipados e ações do jogador.

Dependências:
- `items`: Para manipulação de itens que o jogador pode equipar.

Métodos das Classes:
- `__init__(self, name)`: Inicializa o jogador com um nome e configura valores iniciais para saúde, experiência, inventário, dinheiro, arma e escudo.
- `show_stats(self)`: Exibe as estatísticas atuais do jogador, incluindo saúde, equipamentos e dinheiro.
- `show_status(self)`: Exibe o status completo do jogador, incluindo saúde, equipamentos, inventário e dinheiro.
- `add_item(self, item)`: Adiciona um item ao inventário do jogador.
- `remove_item(self, item)`: Remove um item do inventário do jogador, se ele estiver presente.
- `take_damage(self, damage)`: Reduz a saúde do jogador com base na quantidade de dano recebido. A saúde não pode cair abaixo de zero.
- `earn_money(self, value)`: Adiciona uma certa quantidade de dinheiro ao total do jogador.
- `is_alive(self)`: Verifica se o jogador ainda está vivo com base na saúde atual.
- `equip_item(self, item_index)`: Equipa um item do inventário do jogador se o item for uma arma ou um escudo.
"""

from items import Weapon, Shield, Potion

class Player:
    """
    Representa um jogador no jogo.

    Atributos:
    name (str): O nome do jogador.
    hp (float): A saúde atual do jogador (padrão é 100).
    exp (float): A experiência do jogador.
    inventory (list): O inventário do jogador, contendo os itens que ele possui.
    money (float): A quantidade de dinheiro do jogador.
    weapon (Weapon, opcional): A arma equipada pelo jogador.
    shield (Shield, opcional): O escudo equipado pelo jogador.

    """

    def __init__(self, name):
        """
        Inicializa o jogador com um nome e configura valores iniciais.

        Parâmetros:
        name (str): O nome do jogador.
        """
        self.name = name
        self.hp = 100
        self.exp = 0
        self.inventory = []
        self.money = 0
        self.weapon = None
        self.shield = None

    def show_stats(self):
        """
        Exibe as estatísticas atuais do jogador, incluindo saúde, equipamentos e dinheiro.
        """
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
        print(f"Dinheiro: ${self.money}")

    def show_status(self):
        """
        Exibe o status completo do jogador, incluindo saúde, equipamentos, inventário e dinheiro.
        """
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
        """
        Adiciona um item ao inventário do jogador.

        Parâmetros:
        item (Item): O item a ser adicionado ao inventário.
        """
        self.inventory.append(item)

    def remove_item(self, item):
        """
        Remove um item do inventário do jogador, se ele estiver presente.

        Parâmetros:
        item (Item): O item a ser removido do inventário.
        """
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item não encontrado no inventário.")

    def take_damage(self, damage):
        """
        Reduz a saúde do jogador com base na quantidade de dano recebido. A saúde não pode cair abaixo de zero.

        Parâmetros:
        damage (float): A quantidade de dano a ser reduzida da saúde do jogador.
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def earn_money(self, value):
        """
        Adiciona uma certa quantidade de dinheiro ao total do jogador.

        Parâmetros:
        value (float): A quantidade de dinheiro a ser adicionada.
        """
        self.money += value

    def is_alive(self):
        """
        Verifica se o jogador ainda está vivo com base na saúde atual.

        Retorna:
        bool: Verdadeiro se a saúde do jogador for maior que zero, falso caso contrário.
        """
        return self.hp > 0

    def equip_item(self, item_index):
        """
        Equipa um item do inventário do jogador se o item for uma arma ou um escudo.

        Parâmetros:
        item_index (int): O índice do item no inventário.

        Se o item não puder ser equipado ou o índice for inválido, imprime uma mensagem informativa.
        """
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
