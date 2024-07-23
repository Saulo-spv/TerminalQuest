import os, sys, time, random
from items import Weapon, Potion, Shield, weapons, potions, shields, weight
from enemies import monsters

def print_slow(text, delay=0.0, end = '\n'):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def tutorial(player):
    # Introdução à história
    os.system('cls' if os.name == 'nt' else 'clear') 
    print_slow(f"{player.name}, você é um estudante da EMAP, uma universidade conhecida por seus desafios acadêmicos e atividades extracurriculares intensas. Recentemente, o campus tem sido afetado por estranhas ocorrências: monstros acadêmicos surgem pelos corredores, provas se tornam mais difíceis e até mesmo os professores estão agindo de maneira peculiar. Como um aluno destemido, você decidiu enfrentar esses desafios e restaurar a ordem.")

    print_slow("\nEnquanto explora o campus, você encontra o Professor Vovô, um mentor sábio que oferece ajuda crucial para sua jornada.")
    print_slow(f"\nProfessor Vovô: 'Olá, {player.name}! O campus está enfrentando tempos difíceis com esses monstros acadêmicos à solta. Vou te ajudar a começar sua jornada. Aqui estão alguns itens antigos que podem ser úteis.'")

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

    # Mensagem de entrega de itens
    print_slow(f"\nVocê recebeu: 'Espada velha, Escudo velho e Poção de Cura.'")

    # Orientações adicionais
    print_slow("\nProfessor Vovô: 'Para equipar esses itens, entre no menu apertando 'M' e selecione a opção Equipar com a tecla 'E'.")
    print_slow("\nProfessor Vovô: 'Além disso, você começa com 20 de dinheiro para te ajudar em sua jornada.'")

    print_slow(f"\n{player.name}, sua missão é clara: enfrentar os 7 monstros acadêmicos que estão perturbando o campus. Prepare-se para a aventura e boa sorte na sua jornada para restaurar a paz!")

    print_slow("\nAgora, aventure-se e explore o campus para enfrentar esses desafios e restaurar a ordem!")

def explore(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_slow("\nVocê está explorando o campus...")

    # Chance de encontrar um monstro ou um item
    encounter = random.choices(["monster", "item", "nothing"], weights=[0.3, 0.4, 0.3], k=1)[0]
    
    if encounter == "monster":
        enconter_monster(player)
        
    elif encounter == "item":
        enconter_item(player)

    else:
        print_slow_monsters(monsters)
        print_slow("\nSeus Status atuais")
        player.show_stats()

def print_slow_monsters(monsters):
    if not monsters:
        print_slow("Todos os monstros foram derrotados!")
    else:
        print_slow(f"\nNada por aqui... Parece que os monstros estão se escondendo bem. Continue sua jornada e busque os {len(monsters)} monstros restantes!")
        print_slow("\nMonstros restantes:")
        for monster in monsters:
            print(f"Nome: {monster.name} | Dano: {monster.damage} | HP: {monster.hp}")

def enconter_monster(player):

    monster = random.choice(monsters)
    print_slow("\nVocê encontrou", end = '')
    time.sleep(0.5)
    print_slow(f" .... ", delay=0.2, end = '')
    print_slow(f"{monster.name}!\n", delay=0.015)
    print_slow(monster.description)
    print("\n")
    time.sleep(0.3)

    # Armazena o dano causado e recebido
    player_damage = 0
    monster_damage = 0
    block_amount = 0

    # Loop de combate
    while monster.is_alive() and player.is_alive():
        if player_damage > 0:
            os.system('cls' if os.name == 'nt' else 'clear')

            # Mostra o dano causado no turno anterior
            print_slow(f"\nVocê causou {player_damage} de dano ao {monster.name}.\n")
            print_slow(f"{monster.name} causou {monster_damage} de dano a você. (Seu escudo bloqueou {block_amount})\n")

        
        # Mostra o status atualizado antes do turno
        print("Adversário:")
        monster.show_status()
        
        print_slow("\nStatus do Jogador:")
        player.show_stats()

        print_slow("\nVocê quer abrir o (M)enu, (A)tacar, (C)orrer? ")
        action = input("").lower()

        if action == 'a':
            player_damage, monster_damage, block_amount = attack_monster(player, monster)

        elif action == 'c':
            os.system('cls' if os.name == 'nt' else 'clear') 
            print_slow("\nVocê está prestes a fugir do combate!")
            print_slow("Se você fugir, o monstro retornará ao seu HP normal.")
            confirm = input("Tem certeza que deseja fugir? (S/N): ").lower()
            if confirm == 's':
                # Restaura o HP do monstro para o valor inicial
                monster.restore_hp() 
                print_slow("\nVocê fugiu do combate e o monstro retornou ao seu HP normal.")
                break
            else:
                print_slow("\nVocê decidiu continuar lutando.")

        elif action == 'm':
            menu(player)
        else:
            print_slow("Escolha inválida. Tente novamente.")

def attack_monster(player, monster):
    if player.weapon:
        player_damage = random.randint(int(round(max(player.weapon.damage - 10, 0))), int(round(player.weapon.damage + 10)))
    else:
        player_damage = 1
    monster.take_damage(player_damage)
    
    if not monster.is_alive():
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow(f"Você derrotou {monster.name}!\n")
        print_slow(monster.defeat_message) 
        exp_gained = random.randint(10, 20)
        money_gained = monster.reward
        player.exp += exp_gained
        player.earn_money(money_gained)
        print_slow(f"Você ganhou {exp_gained} de experiência e ${money_gained} de dinheiro.")
        monsters.remove(monster)
        if not monsters:
            print_slow("\nParabéns! Você venceu todos os monstros acadêmicos e trouxe paz de volta ao campus. Sua coragem e determinação foram inspiradoras. Com a ordem restaurada, os alunos podem agora focar em seus estudos e projetos sem interrupções. Que sua jornada continue cheia de sucesso e aventuras. Até a próxima grande conquista!")
            print_slow("\nComo prêmio você ganhara um chocolate!!!\n")
            return [0, 0, 0]

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
        print_slow("Você foi derrotado!")
        print_slow("\nVocê enfrentou muitos desafios e lutou bravamente, mas infelizmente não conseguiu superar todos os obstáculos desta vez. O campus ficou sob a influência dos monstros e os alunos enfrentaram dificuldades. Lembre-se, cada desafio é uma oportunidade para aprender e crescer. Volte mais forte e preparado para a próxima jornada. Até a próxima aventura!")
        print_slow(f"\nTodos lembraram da bravura de {player.name}!!!")
        print_slow("\nComo castigo você deve um chocolate ao Saulo!!!\n")
        return [0, 0, 0]
    
    return [player_damage, monster_damage, block_amount]

def enconter_item(player):
    # Escolhe aleatoriamente um tipo de item (espada, escudo ou poção)
    item_type = random.choice(["weapon", "shield", "potion"])
    
    if item_type == "weapon":
        config = random.choices(weapons, weights=weight)[0]
        item = Weapon(config[0], config[1], config[2])
    elif item_type == "shield":
        config = random.choices(shields, weights=weight)[0]
        item = Shield(config[0], config[1], config[2])
    else:
        config = random.choices(potions, weights=weight)[0]
        item = Potion(config[0], config[1], config[2])

    print_slow("\nVocê encontrou", end = '')
    time.sleep(0.5)
    print_slow(f" .... ", delay=0.2, end = '')
    print_slow(f"{item.name}!\n", delay=0.015)
    time.sleep(0.3)
    player.add_item(item)
    print_slow(f"{item.name} foi adicionado ao seu inventário. \n")
    player.show_status()

def menu(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow("\nVocê está no Menu...\n")
        player.show_status()
        print_slow("\nO que você quer fazer? (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção, (S)air do Menu: ")
        action = input("").lower()
        
        if action == 'e':
            equip_item(player)
        
        elif action == 'v':
            sell_item(player)
        
        elif action == 'u':
            upgrade_item(player)
        
        elif action == 'p':
            use_potion(player)

        elif action == 's':
            print_slow("Saindo do menu.")
            os.system('cls' if os.name == 'nt' else 'clear') 
            break

        else:
            print_slow("Escolha inválida. Por favor, escolha (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção ou (S)air do Menu.")
            print_slow("Pressione 'Enter' para voltar!")
            input("")

def equip_item(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow("Seus status atuais")
        player.show_stats()
        print_slow("\nItens disponíveis para equipar:")
        for idx, item in enumerate(player.inventory):
            if not isinstance(item, Potion):
                print(f"[{idx + 1}] {item}")

        print_slow("\nDigite o número do item que deseja equipar ou (v) para voltar: ")
        action = input("").lower()
        if action == 'v':
            break
        
        try:
            item_index = int(action) - 1
            if 0 <= item_index < len(player.inventory):
                player.equip_item(item_index)
                if not (isinstance(player.inventory[item_index], Potion)):
                    print_slow(f"\nVocê equipou {player.inventory[item_index].name}.")
            else:
                print_slow("Índice do item não encontrado no inventário.")
        except ValueError:
            print_slow("Por favor, insira um número válido.")
        
        print_slow("\nPressione Enter para voltar ao menu.")
        input("")

def sell_item(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 

        print_slow("Seus status atuais")
        player.show_stats()
        print_slow("\nItens disponíveis para venda:")
        for idx, item in enumerate(player.inventory):
            print(f"[{idx + 1}] {item}")

        print_slow("\nDigite o número do item que deseja vender ou (v) para voltar: ")
        action = input("").lower()
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
                print_slow(f"\nVocê vendeu {item_to_sell.name} por ${item_to_sell.value}.")
            else:
                print_slow("Índice do item não encontrado no inventário.")
        except ValueError:
            print_slow("Por favor, insira um número válido.")
        
        print_slow("\nPressione Enter para voltar ao menu.")
        input("")

def upgrade_item(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print_slow("Seus status atuais")
        player.show_stats()

        print_slow("\nItens disponíveis para upgrade:")

        for idx, item in enumerate(player.inventory):
            if isinstance(item, Weapon):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Dano atual: {item.damage:.2f}, Dano após upgrade: {item.calculate_next_damage():.2f}")
            elif isinstance(item, Shield):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Bloqueio atual: {item.block_amount:.2f}, Bloqueio após upgrade: {item.calculate_next_block():.2f}")
            elif isinstance(item, Potion):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Cura atual: {item.heal_amount:.2f}, Cura após upgrade: {item.calculate_next_heal():.2f}")
        
        print_slow("\nDigite o número do item que deseja melhorar ou (v) para voltar: ")
        action = input("").lower()
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
                        print_slow(f"\nVocê melhorou {item_to_upgrade.name} para nível {item_to_upgrade.level}.")
                else:
                    print_slow("Dinheiro insuficiente para o upgrade.")
            else:
                print_slow("Índice do item não encontrado no inventário.")
        except ValueError:
            print_slow("Por favor, insira um número válido.")
        
        print_slow("\nPressione Enter para voltar ao menu.")
        input("")

def use_potion(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow("Lembre-se que o hp máx é 100, então o excedente de cura será desperdiçado!!!\n")
        print_slow("Seus status atuais")
        player.show_stats()
        print_slow("\nPoções disponíveis para uso:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Potion):
                print(f"[{idx + 1}] {item}")

        print_slow("\nDigite o número da poção que deseja usar ou (v) para voltar: ")
        action = input("").lower()
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
                    print_slow(f"\nVocê usou {potion_to_use.name}.")
                    player.inventory.pop(item_index)
                else:
                    print_slow("O item selecionado não é uma poção.")
            else:
                print_slow("Índice do item não encontrado no inventário.")
        except ValueError:
            print_slow("Por favor, insira um número válido.")
        
        print_slow("\nPressione Enter para voltar ao menu.")
        input("")