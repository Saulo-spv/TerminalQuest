from player import Player
from items import Weapon, Potion, Shield

def tutorial(player):

    # Introdução à história
    print("\nPrimeiramente, você decide explorar o campus para entender o que está acontecendo.")
    print("Enquanto caminha pelos corredores, você se encontra com o Professor Vovô.")
    print("\nProfessor Vovô: 'Olá, jovem! O campus está enfrentando tempos difíceis, com monstros acadêmicos à solta. Eu vou te ajudar a começar sua jornada. Aqui estão alguns itens básicos para te ajudar'")
    
    # Criando itens iniciais
    sword = Weapon("Espada de Treinamento", 10, 5)
    shield = Shield("Escudo de Treinamento", 5, 2)
    potion = Potion("Poção de Cura", 3, 10)

    # Adicionando itens ao inventário do jogador
    player.add_item(sword)
    player.add_item(shield)
    player.add_item(potion)

    # Professor Vovô dando dinheiro
    player.earn_money(50)
    
    # Equipando itens iniciais
    print("\nProfessor Vovô: 'Agora, deixe-me te ensinar como equipar esses itens. Entre no menu apertando 'M' depois selecione Equipar com a tecla 'e'!")

    print("\nProfessor Vovô: 'Você também receberá 50 de dinheiro para começar sua jornada.'")
    print("\nVocê está pronto para explorar o campus e enfrentar os desafios!")


def explore(player):
    print("\nVocê está explorando o campus...")
    # Aqui você pode adicionar o código para encontrar monstros, itens ou desafios

def inventory(player):
    print("\nAbrindo inventário...")
    player.show_status()

    # Loop principal do inventário
    action = None
    while action != 's':
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
