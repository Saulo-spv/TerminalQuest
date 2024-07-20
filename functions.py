from player import Player
from items import Weapon, Potion, Shield

def explore(player):
    print("\nVocê está explorando o campus...")
    # Aqui você pode adicionar o código para encontrar monstros, itens ou desafios

def inventory(player):
    print("\nAbrindo inventário...")
    player.show_status()

    # Loop principal do inventário
    while player.is_alive():
        action = input("\nO que você quer fazer? (E)quipar item, (V)ender item, (S)air: ").lower()
        if action == 'e':
            try:
                item_index = int(input("Digite o número do item que deseja equipar: ")) - 1
                player.equip_item(item_index)
                player.show_status()
            except ValueError:
                print("Por favor, insira um número válido.")
        elif action == 'v':
            try:
                item_index = int(input("Digite o número do item que deseja vender: ")) - 1
                if 0 <= item_index < len(player.inventory):
                    item_to_sell = player.inventory[item_index]

                    # Verifica se o item vendido está equipado e desequipa se necessário
                    if player.weapon == item_to_sell:
                        player.weapon = None
                    if player.shield == item_to_sell:
                        player.shield = None

                    player.inventory.pop(item_index)
                    player.earn_money(item_to_sell.value)
                    print(f"Você vendeu {item_to_sell.name} por ${item_to_sell.value}.")
                    player.show_status()
                else:
                    print("Índice do item não encontrado no inventário.")
            except ValueError:
                print("Por favor, insira um número válido.")
            break
        else:
            print("Escolha inválida. Por favor, escolha (E)quipar item, (V)ender item ou (S)air.")
