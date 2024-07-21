import random
import os
from player import Player
from items import Weapon, Potion, Shield, weapons, potions, shields, weight
from enemies import monsters

def tutorial(player):
    # Introdução à história
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f"{player.name}, você é um estudante da EMAP, uma universidade conhecida por seus desafios acadêmicos e atividades extracurriculares intensas. Recentemente, o campus tem sido afetado por estranhas ocorrências: monstros acadêmicos surgem pelos corredores, provas se tornam mais difíceis e até mesmo os professores estão agindo de maneira peculiar. Como um aluno destemido, você decidiu enfrentar esses desafios e restaurar a ordem.")

    print("\nEnquanto explora o campus, você encontra o Professor Vovô, um mentor sábio que oferece ajuda crucial para sua jornada.")
    print(f"\nProfessor Vovô: 'Olá, {player.name}! O campus está enfrentando tempos difíceis com esses monstros acadêmicos à solta. Vou te ajudar a começar sua jornada. Aqui estão alguns itens antigos que podem ser úteis.'")
        
    # Criando itens iniciais
    sword = Weapon("Espada velha", 10, 7)
    shield = Shield("Escudo velho", 5, 2)
    potion = Potion("Poção de Cura", 3, 10)

    # Adicionando itens ao inventário do jogador
    player.add_item(sword)
    player.add_item(shield)
    player.add_item(potion)

    # Professor Vovô dando dinheiro
    player.earn_money(20)
        
    # Equipando itens iniciais
    print("\nProfessor Vovô: 'Para equipar esses itens, entre no menu apertando 'M' e selecione a opção Equipar com a tecla 'E'.")
    print("\nProfessor Vovô: 'Além disso, você começa com 20 de dinheiro para te ajudar em sua jornada.'")

    print(f"\n{player.name}, sua missão é clara: enfrentar os 7 monstros acadêmicos que estão perturbando o campus. Prepare-se para a aventura e boa sorte na sua jornada para restaurar a paz!")

    print("\nAgora, aventure-se e explore o campus para enfrentar esses desafios e restaurar a ordem!")

def explore(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nVocê está explorando o campus...")

    # Chance de encontrar um monstro ou um item
    encounter = random.choice(["monster", "item", "nothing"])
    
    if encounter == "monster":
        monster = random.choice(monsters)
        print(f"\nVocê encontrou {monster.name}!")
        print(monster.description)
        
        # Variável para controlar se é o primeiro turno
        first_turn = True

        # Armazena o dano causado e recebido
        player_damage = 0
        damage_to_player = 0
        block_amount = 0

        # Loop de combate
        while monster.is_alive() and player.is_alive():
            if not first_turn:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela a cada turno após o primeiro

                # Mostra o dano causado no turno anterior
                print(f"\nVocê causou {player_damage} de dano ao {monster.name}.")
                print(f"{monster.name} causou {damage_to_player} de dano a você. (Seu escudo bloqueou {block_amount})")

            
            # Mostra o status atualizado antes do turno
            monster.show_status()
            
            print("\nStatus do Jogador:")
            player.show_stats()

            action = input("Você quer abrir o (M)enu, (A)tacar, (C)orrer? ").lower()
            if action == 'a':
                # Jogador ataca o monstro
                if player.weapon:
                    player_damage = random.randint(int(round(max(player.weapon.damage - 10, 0))), int(round(player.weapon.damage + 10)))
                else:
                    player_damage = 1
                monster.take_damage(player_damage)
                
                if not monster.is_alive():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print(f"Você derrotou {monster.name}!\n")
                    print(monster.defeat_message) 
                    exp_gained = random.randint(10, 20)
                    money_gained = monster.reward
                    player.exp += exp_gained
                    player.earn_money(money_gained)
                    print(f"Você ganhou {exp_gained} de experiência e ${money_gained} de dinheiro.")
                    monsters.remove(monster)
                    if not monsters:
                        print("Parabéns! Você venceu todos os monstros acadêmicos e trouxe paz de volta ao campus. Sua coragem e determinação foram inspiradoras. Com a ordem restaurada, os alunos podem agora focar em seus estudos e projetos sem interrupções. Que sua jornada continue cheia de sucesso e aventuras. Até a próxima grande conquista!")
                    break

                # Monstro ataca o jogador
                monster_damage = random.randint(max(monster.damage - 10, 0), monster.damage + 10)
                if player.shield:
                    # Calcula o bloqueio com um range aleatório
                    block_amount = random.randint(int(round(max(player.shield.block_amount - 5, 0))), int(round(player.shield.block_amount + 5)))
                    damage_to_player = max(monster_damage - block_amount, 0)
                else:
                    damage_to_player = monster_damage

                player.take_damage(damage_to_player)
                
                if not player.is_alive():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print("Você foi derrotado!")
                    print("\nVocê enfrentou muitos desafios e lutou bravamente, mas infelizmente não conseguiu superar todos os obstáculos desta vez. O campus ficou sob a influência dos monstros e os alunos enfrentaram dificuldades. Lembre-se, cada desafio é uma oportunidade para aprender e crescer. Volte mais forte e preparado para a próxima jornada. Até a próxima aventura!")
                    print(f"\nTodos lembraram da bravura de {player.name}!!!")
                    break
            elif action == 'c':
                print("\nVocê fugiu do combate!")
                break
            elif action == 'm':
                menu(player)
            else:
                print("Escolha inválida. Tente novamente.")
            first_turn = False

    elif encounter == "item":
        # Escolhe aleatoriamente um tipo de item (espada, escudo ou poção)
        item_type = random.choice(["sword", "shield", "potion"])
        if item_type == "sword":
            item = random.choices(weapons, weights = weight)[0]
        elif item_type == "shield":
            item = random.choices(shields, weights = weight)[0]
        else:
            item = random.choices(potions, weights= weight)[0]

        print(f"\nVocê encontrou um {item.name}!")
        player.add_item(item)
        print(f"{item.name} foi adicionado ao seu inventário.")
        player.show_status()
    else:
        print(f"\nNada por aqui... Parece que os monstros estão se escondendo bem. Continue sua jornada e busque os {len(monsters)} monstros restantes!")



def menu(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nVocê está no Menu...\n")
        player.show_status()
        action = input("\nO que você quer fazer? (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção, (S)air do Menu: ").lower()
        
        if action == 'e':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Seus status atuais")
                player.show_stats()
                print("\nItens disponíveis para equipar:")
                for idx, item in enumerate(player.inventory):
                    print(f"[{idx + 1}] {item}")

                action = input("\nDigite o número do item que deseja equipar ou (v) para voltar: ").lower()
                if action == 'v':
                    break
                
                try:
                    item_index = int(action) - 1
                    if 0 <= item_index < len(player.inventory):
                        player.equip_item(item_index)
                        if not (isinstance(player.inventory[item_index], Potion)):
                            print(f"\nVocê equipou {player.inventory[item_index].name}.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")
        
        elif action == 'v':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Seus status atuais")
                player.show_stats()
                print("\nItens disponíveis para venda:")
                for idx, item in enumerate(player.inventory):
                    print(f"[{idx + 1}] {item}")

                action = input("\nDigite o número do item que deseja vender ou (v) para voltar: ").lower()
                if action == 'v':
                    break
                
                try:
                    item_index = int(action) - 1
                    if 0 <= item_index < len(player.inventory):
                        item_to_sell = player.inventory[item_index]
                        
                        # Verifica se o item vendido está equipado e desequipa se necessário
                        if player.weapon == item_to_sell:
                            player.weapon = None
                        if player.shield == item_to_sell:
                            player.shield = None

                        player.inventory.pop(item_index)
                        player.earn_money(item_to_sell.value)
                        print(f"\nVocê vendeu {item_to_sell.name} por ${item_to_sell.value}.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")
        
        elif action == 'u':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')  
                print("Seus status atuais")
                player.show_stats()

                print("\nItens disponíveis para upgrade:")

                for idx, item in enumerate(player.inventory):
                    if isinstance(item, Weapon):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Dano atual: {item.damage:.2f}, Dano após upgrade: {item.calculate_next_damage():.2f}")
                    elif isinstance(item, Shield):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Bloqueio atual: {item.block_amount:.2f}, Bloqueio após upgrade: {item.calculate_next_block():.2f}")
                    elif isinstance(item, Potion):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Cura atual: {item.heal_amount:.2f}, Cura após upgrade: {item.calculate_next_heal():.2f}")
                
                action = input("\nDigite o número do item que deseja melhorar ou (v) para voltar: ").lower()
                if action == 'v':
                    break
                
                try:
                    item_index = int(action) - 1
                    if 0 <= item_index < len(player.inventory):
                        item_to_upgrade = player.inventory[item_index]
                        # Verifique se o jogador tem dinheiro suficiente e faça o upgrade
                        upgrade_cost = item_to_upgrade.value * 1.5
                        if player.money >= upgrade_cost:
                                item_to_upgrade.upgrade()
                                player.earn_money(-upgrade_cost)
                                print(f"\nVocê melhorou {item_to_upgrade.name} para nível {item_to_upgrade.level}.")
                        else:
                            print("Dinheiro insuficiente para o upgrade.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")
        
        elif action == 'p':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Seus status atuais")
                player.show_stats()
                print("\nPoções disponíveis para uso:")
                for idx, item in enumerate(player.inventory):
                    if isinstance(item, Potion):
                        print(f"[{idx + 1}] {item}")

                action = input("\nDigite o número da poção que deseja usar ou (v) para voltar: ").lower()
                if action == 'v':
                    break
                
                try:
                    item_index = int(action) - 1
                    if 0 <= item_index < len(player.inventory):
                        potion_to_use = player.inventory[item_index]
                        if isinstance(potion_to_use, Potion):
                            # Atualiza o HP com valor float e arredonda para duas casas decimais
                            player.hp = min(100.0, round(player.hp + potion_to_use.heal_amount, 2))
                            player.show_status()
                            print(f"\nVocê usou {potion_to_use.name}.")
                            player.inventory.pop(item_index)
                        else:
                            print("O item selecionado não é uma poção.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")

        elif action == 's':
            print("Saindo do menu.")
            break

        else:
            print("Escolha inválida. Por favor, escolha (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção ou (S)air do Menu.")
