import random
import os
from player import Player
from items import Weapon, Potion, Shield, weapons, potions, shields, weight
from enemies import monsters

def tutorial(player):
    os.system('cls' if os.name == 'nt' else 'clear') 
    # Introdução à história
    print(f"{player.name}, você é um estudante da EMAP, conhecida por seus desafios acadêmicos e atividades extracurriculares intensas. Recentemente, estranhas ocorrências começaram a afetar o campus: monstros acadêmicos surgem nos corredores, provas se tornam mais difíceis e até mesmo professores parecem estar agindo de maneira peculiar. Você, como um aluno destemido, decide enfrentar esses desafios e restaurar a ordem no campus.")
    print("\nPrimeiramente, você decide explorar o campus para entender o que está acontecendo.")
    print("Enquanto caminha pelos corredores, você se encontra com o Professor Vovô.")
    print("\nProfessor Vovô: 'Olá, jovem! O campus está enfrentando tempos difíceis, com monstros acadêmicos à solta. Eu vou te ajudar a começar sua jornada. Aqui estão alguns itens básicos para te ajudar'")
    
    # Criando itens iniciais
    sword = Weapon("Espada velha", 10, 5)
    shield = Shield("Escudo velho", 5, 2)
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

        # Loop de combate
        while monster.is_alive() and player.is_alive():
            if not first_turn:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela a cada turno após o primeiro
            first_turn = False

            # Mostra o dano causado no turno anterior
            if player_damage > 0:
                print(f"\nVocê causou {player_damage} de dano ao {monster.name}.")
            if damage_to_player > 0:
                print(f"{monster.name} causou {damage_to_player} de dano a você. (Seu escudo bloqueou {block_amount})")
            
            # Mostra o status atualizado antes do turno
            monster.show_status()
            
            print("\nStatus do Jogador:")
            player.show_stats()

            action = input("Você quer abrir o (M)enu, (A)tacar, (C)orrer? ").lower()
            if action == 'a':
                # Jogador ataca o monstro
                if player.weapon:
                    player_damage = random.randint(max(player.weapon.damage - 10, 0), player.weapon.damage + 10)
                else:
                    player_damage = 1
                monster.take_damage(player_damage)
                
                if not monster.is_alive():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print(f"Você derrotou {monster.name}!")
                    exp_gained = random.randint(10, 20)
                    money_gained = random.randint(20, 50)
                    player.exp += exp_gained
                    player.earn_money(money_gained)
                    print(f"Você ganhou {exp_gained} de experiência e ${money_gained} de dinheiro.")
                    monsters.remove(monster)
                    if not monsters:
                        print("Parabens você derrotou todos os monstros academicos!")
                    break

                # Monstro ataca o jogador
                monster_damage = random.randint(max(monster.damage - 10, 0), monster.damage + 10)
                if player.shield:
                    # Calcula o bloqueio com um range aleatório
                    block_amount = random.randint(max(player.shield.block_amount - 5, 0), player.shield.block_amount + 5)
                    damage_to_player = max(monster_damage - block_amount, 0)
                else:
                    damage_to_player = monster_damage

                player.take_damage(damage_to_player)
                
                if not player.is_alive():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print("Você foi derrotado, assim todos os alunos foram reprovados e os monstros saíram vencedores. FIM DE JOGO!")
                    break
            elif action == 'c':
                print("Você fugiu do combate!")
                break
            elif action == 'm':
                menu(player)
            else:
                print("Escolha inválida. Tente novamente.")

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
        print("\nVocê não encontrou nada desta vez. Continue explorando!")


def menu(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nVocê está no Menu...\n")
        player.show_status()
        action = input("\nO que você quer fazer? (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção, (S)air: ").lower()
        
        if action == 'e':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
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
                        player.show_status()
                        print(f"\nVocê equipou {player.inventory[item_index].name}.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")
        
        elif action == 'v':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
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
                        player.show_status()
                        print(f"\nVocê vendeu {item_to_sell.name} por ${item_to_sell.value}.")
                    else:
                        print("Índice do item não encontrado no inventário.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                
                input("\nPressione Enter para voltar ao menu.")
        
        elif action == 'u':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("\nItens disponíveis para upgrade:")
                for idx, item in enumerate(player.inventory):
                    if isinstance(item, Weapon):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 0.5}, Nível atual: {item.level}, Dano atual: {item.damage}, Dano após upgrade: {item.damage + 5}")
                    elif isinstance(item, Potion):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 0.5}, Nível atual: {item.level}, Cura atual: {item.heal_amount}, Cura após upgrade: {item.heal_amount + 10}")
                    elif isinstance(item, Shield):
                        print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 0.5}, Nível atual: {item.level}, Bloqueio atual: {item.block_amount}, Bloqueio após upgrade: {item.block_amount + 3}")

                action = input("\nDigite o número do item que deseja melhorar ou (v) para voltar: ").lower()
                if action == 'v':
                    break
                
                try:
                    item_index = int(action) - 1
                    if 0 <= item_index < len(player.inventory):
                        item_to_upgrade = player.inventory[item_index]
                        # Verifique se o jogador tem dinheiro suficiente e faça o upgrade
                        upgrade_cost = item_to_upgrade.value * 0.5
                        if player.money >= upgrade_cost:
                                item_to_upgrade.upgrade()
                                player.earn_money(-upgrade_cost)
                                player.show_status()
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
                            player.hp = min(100, player.hp + potion_to_use.heal_amount)
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
            print("Escolha inválida. Por favor, escolha (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção ou (S)air.")
