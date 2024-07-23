"""
Módulo `functions`

Este módulo contém funções para gerenciar e interagir com um jogo de RPG baseado em texto.

As funções neste módulo permitem que o jogador:

1. Explore o campus e encontre monstros ou itens.
2. Enfrente e ataque monstros.
3. Equipe e venda itens.
4. Utilize potions e faça upgrades em itens.
5. Interaja com o menu principal do jogo e execute diversas ações.
6. Execute um tutorial que fornece uma introdução e itens iniciais ao jogador.
7. Exiba informações detalhadas sobre monstros restantes e o status do jogador.

Funções:
- `tutorial(player)`: Fornece uma introdução ao jogo e itens iniciais ao jogador.
- `print_slow(text, delay=0.0, end='\n')`: Imprime o texto no terminal com um efeito de digitação lenta.
- `explore(player)`: Permite que o jogador explore o campus e encontre monstros, itens ou nada.
- `print_slow_monsters(monsters)`: Exibe informações sobre os monstros restantes no jogo.
- `enconter_monster(player)`: Gerencia o encontro com um monstro aleatório.
- `attack_monster(player)`: Gerencia o combate com um monstro aleatório.
- `enconter_item(player)`: Gerencia o encontro de um item durante a exploração, adicionando-o ao inventário do jogador.
- `menu(player)`: Exibe o menu principal do jogo e permite que o jogador escolha ações como equipar itens, vender itens, fazer upgrades, usar poções ou sair do menu.
- `equip_item(player)`: Permite que o jogador equipe um item do inventário.
- `sell_item(player)`: Permite que o jogador venda um item do inventário e ganhe dinheiro.
- `upgrade_item(player)`: Permite que o jogador faça upgrade de um item no inventário, aumentando suas estatísticas.
- `use_potion(player)`: Permite que o jogador use uma poção do inventário para restaurar a saúde.

Dependências:
- `os`: Para limpar a tela do terminal.
- `sys`: Para operações de entrada/saída.
- `time`: Para adicionar delays na exibição do texto.
- `random`: Para gerar encontros e probabilidades aleatórias.
- `items`: Para as classes `Weapon`, `Potion`, `Shield`, e as listas de itens `weapons`, `potions`, `shields`, `weight`.
- `enemies`: Para a lista de `monsters`.

"""

import os, sys, time, random
from items import Weapon, Potion, Shield, weapons, potions, shields, weight
from enemies import monsters

def print_slow(text, delay=0.01, end='\n'):
    """
    Imprime o texto caracter por caracter com um atraso opcional entre cada caractere.

    A função simula uma impressão mais lenta para criar um efeito de digitação no terminal.

    Parâmetros:
    text (str): O texto a ser impresso. Cada caractere será exibido um de cada vez.
    delay (float, opcional): O tempo de atraso em segundos entre a impressão de cada caractere. O padrão é 0.015 segundos.
    end (str, opcional): O caractere a ser adicionado ao final da impressão, como uma nova linha ('\n') 
    ou qualquer outro caractere. O padrão é '\n'.

    Comportamento:
    - Itera sobre cada caractere da string `text`.
    - Imprime cada caractere com um atraso especificado por `delay`.
    - Adiciona o caractere final `end` ao final do texto.

    """
    # Itera sobre cada caractere na string de texto
    for char in text:
        # Escreve o caractere atual no buffer de saída
        sys.stdout.write(char)
        # Garante que o caractere seja imediatamente exibido na tela
        sys.stdout.flush()
        # Pausa a execução por um tempo especificado antes de imprimir o próximo caractere
        time.sleep(delay)
    # Adiciona o caractere final (como uma nova linha) ao final da impressão
    sys.stdout.write(end)
    # Garante que o caractere final seja exibido
    sys.stdout.flush()

def tutorial(player):
    """
    Fornece uma introdução ao jogo e orientações iniciais para o jogador.

    A função realiza os seguintes passos:
    1. Limpa a tela do terminal para iniciar o tutorial.
    2. Exibe uma introdução à história, apresentando o jogador e o contexto do jogo.
    3. Apresenta o Professor Vovô, um mentor que oferece ajuda crucial ao jogador.
    4. Cria e adiciona itens iniciais ao inventário do jogador (uma espada, um escudo e uma poção).
    5. Concede uma quantia inicial de dinheiro ao jogador.
    6. Fornece orientações sobre como equipar itens e o objetivo do jogo.
    7. Finaliza com uma mensagem de encorajamento e instrução para começar a aventura.

    Parâmetros:
    player (Player): O objeto `Player` que representa o jogador atual. Deve possuir métodos `add_item()` e `earn_money()` e atributos relacionados ao status do jogador.

    Comportamento:
    - A função limpa a tela e apresenta a história do jogo.
    - Introduz o Professor Vovô e fornece itens e dinheiro iniciais ao jogador.
    - Dá orientações sobre como usar o menu e o objetivo da missão.

    """
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
    """
    Simula a exploração do campus pelo jogador, determinando aleatoriamente o que o jogador encontra.

    A função realiza os seguintes passos:
    1. Limpa a tela do terminal para uma nova exploração.
    2. Exibe uma mensagem informando que o jogador está explorando.
    3. Determina aleatoriamente se o jogador encontra um monstro, um item ou nada.
    4. Dependendo do resultado da determinação:
       - Se encontrar um monstro, chama a função `enconter_monster` para lidar com o combate.
       - Se encontrar um item, chama a função `enconter_item` para adicionar o item ao inventário.
       - Se não encontrar nada, exibe os status dos monstros restantes no campus e os status atuais do jogador.

    Parâmetros:
    player (Player): O objeto `Player` que representa o jogador atual.

    Comportamento:
    - A função exibe uma mensagem de exploração e usa uma escolha aleatória para determinar o encontro.
    - Dependendo do encontro, o jogador pode lutar contra um monstro, receber um item ou simplesmente revisar o status atual.

    """
    # Limpa a tela do terminal para uma nova exploração
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Mensagem inicial informando que o jogador está explorando
    print_slow("\nVocê está explorando o campus...")

    # Chance de encontrar um monstro, um item ou nada
    encounter = random.choices(["monster", "item", "nothing"], weights=[0.3, 0.4, 0.3], k=1)[0]
    
    if encounter == "monster":
        # Se o encontro for um monstro, chama a função para lidar com o monstro
        enconter_monster(player)
        
    elif encounter == "item":
        # Se o encontro for um item, chama a função para lidar com o item
        enconter_item(player)

    else:
        # Se o encontro for "nothing", apenas exibe os status do jogador e os monstros no campus
        print_slow_monsters(monsters)
        print_slow("\nSeus Status atuais")
        player.show_stats()

def print_slow_monsters(monsters):
    """
    Exibe uma lista dos monstros restantes na jornada do jogador.

    A função realiza os seguintes passos:
    1. Exibe uma mensagem informando quantos monstros restantes ainda precisam ser encontrados.
    2. Mostra a lista de monstros restantes com detalhes sobre cada um.

    Parâmetros:
    monsters (list): Uma lista de objetos `Monster` que representam os monstros restantes na jornada. 
    Cada objeto deve ter os atributos `name`, `damage`, e `hp`.

    Comportamento:
    - A função exibe uma mensagem informativa indicando o número de monstros restantes.
    - Em seguida, exibe uma lista dos monstros restantes, incluindo o nome, dano e HP de cada um.

    """
    # Se ainda há monstros restantes, exibe uma mensagem informando quantos monstros restam
    print_slow(f"\nNada por aqui... Parece que os monstros estão se escondendo bem. Continue sua jornada e busque os {len(monsters)} monstros restantes!")
    
    # Exibe a lista dos monstros restantes com detalhes
    print_slow("\nMonstros restantes:")
    for monster in monsters:
        # Imprime informações sobre cada monstro (nome, dano e HP)
        print(f"Nome: {monster.name} | Dano: {monster.damage} | HP: {monster.hp}")

def enconter_monster(player):
    """
    Simula um encontro e combate com um monstro aleatório.

    A função realiza os seguintes passos:
    1. Seleciona aleatoriamente um monstro da lista de monstros.
    2. Exibe uma mensagem de encontro com o monstro e sua descrição.
    3. Inicia um loop de combate onde o jogador e o monstro se atacam alternadamente.
    4. Durante o combate, exibe o status atualizado do monstro e do jogador.
    5. Solicita ao jogador uma ação: atacar, correr ou abrir o menu.
    6. Se o jogador optar por atacar, a função `attack_monster` é chamada para realizar o ataque.
    7. Se o jogador optar por correr, confirma a intenção de fuga e, se confirmada, restaura o HP do monstro e encerra o combate.
    8. Se o jogador optar por abrir o menu, a função `menu` é chamada.
    9. Se o jogador escolher uma opção inválida, exibe uma mensagem de erro e solicita uma nova entrada.

    Parâmetros:
    player (Player): O objeto que representa o jogador, que participará do combate e tomará as decisões.

    Comportamento:
    - Um monstro é escolhido aleatoriamente da lista `monsters` e sua descrição é exibida.
    - O combate continua até que o monstro ou o jogador sejam derrotados ou o jogador escolha correr.
    - O dano causado e recebido é atualizado e exibido após cada ação do jogador.
    - O jogador pode escolher entre atacar, correr ou abrir o menu. O combate é encerrado se o jogador fugir ou for derrotado.

    """
    # Seleciona aleatoriamente um monstro da lista de monstros
    monster = random.choice(monsters)
    
    # Mensagem de encontro com o monstro
    print_slow("\nVocê encontrou", end='')
    time.sleep(0.5)
    print_slow(f" .... ", delay=0.2, end='')
    print_slow(f"{monster.name}!\n", delay=0.015)
    print_slow(monster.description)
    print("\n")
    time.sleep(0.3)

    # Inicializa as variáveis para armazenar o dano causado e recebido
    player_damage = 0
    monster_damage = 0
    block_amount = 0

    # Loop de combate
    while monster.is_alive() and player.is_alive():
        if player_damage > 0:
            # Limpa a tela para mostrar o estado atual do combate
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Mostra o dano causado no turno anterior
            print_slow(f"\nVocê causou {player_damage} de dano ao {monster.name}.\n")
            print_slow(f"{monster.name} causou {monster_damage} de dano a você. (Seu escudo bloqueou {block_amount})\n")

        # Mostra o status atualizado do monstro e do jogador
        print("Adversário:")
        monster.show_status()
        
        print_slow("\nStatus do Jogador:")
        player.show_stats()

        # Solicita a ação do jogador
        print_slow("\nVocê quer abrir o (M)enu, (A)tacar, (C)orrer? ")
        action = input("").lower()

        if action == 'a':
            # Se o jogador optar por atacar, chama a função de ataque
            player_damage, monster_damage, block_amount = attack_monster(player, monster)

        elif action == 'c':
            # Se o jogador optar por correr, confirma se deseja realmente fugir
            os.system('cls' if os.name == 'nt' else 'clear') 
            print_slow("\nVocê está prestes a fugir do combate!")
            print_slow("Se você fugir, o monstro retornará ao seu HP normal.")
            confirm = input("Tem certeza que deseja fugir? (S/N): ").lower()
            if confirm == 's':
                # Restaura o HP do monstro ao valor inicial e encerra o combate
                monster.restore_hp() 
                print_slow("\nVocê fugiu do combate e o monstro retornou ao seu HP normal.")
                break
            else:
                print_slow("\nVocê decidiu continuar lutando.")

        elif action == 'm':
            # Se o jogador optar pelo menu, chama a função de menu
            menu(player)
        else:
            # Caso o jogador insira uma opção inválida, exibe uma mensagem de erro
            print_slow("Escolha inválida. Tente novamente.")

def attack_monster(player, monster):
    """
    Simula um turno de combate entre o jogador e um monstro.

    A função realiza os seguintes passos:
    1. Calcula o dano causado pelo jogador ao monstro, com base na arma equipada (se houver).
    2. Aplica o dano ao monstro e verifica se o monstro foi derrotado.
    3. Se o monstro for derrotado, o jogador ganha experiência e dinheiro e o monstro é removido da lista.
    4. Se o jogador for derrotado, exibe uma mensagem de derrota e retorna uma lista de zero valores.
    5. Calcula o dano causado pelo monstro ao jogador, considerando o escudo (se houver) e aplica o dano ao jogador.
    6. Retorna o dano causado pelo jogador, o dano causado pelo monstro e o bloqueio do escudo.

    Parâmetros:
    player (Player): O objeto que representa o jogador, que realizará o ataque e receberá o dano.
    monster (Monster): O objeto que representa o monstro, que será atacado e causará dano ao jogador.

    Comportamento:
    - Se o jogador tiver uma arma equipada, o dano causado ao monstro é um valor aleatório dentro de um intervalo baseado na arma. 
    Caso contrário, o dano é mínimo (1).
    - Se o monstro for derrotado, o jogador ganha experiência e dinheiro, e o monstro é removido da lista de monstros. 
    Se todos os monstros forem derrotados, uma mensagem de vitória é exibida.
    - O monstro ataca o jogador com dano variável. Se o jogador tiver um escudo, o dano é reduzido com base na quantidade de bloqueio do escudo. 
    O dano efetivo recebido pelo jogador é calculado e aplicado.
    - Se o jogador for derrotado, uma mensagem de derrota é exibida e o jogo termina.

    Retorna:
    list: Uma lista contendo três valores:
        - O dano causado pelo jogador ao monstro.
        - O dano causado pelo monstro ao jogador.
        - O valor do bloqueio do escudo, se o jogador estiver usando um escudo.

    Exceções:
    - Esta função não levanta exceções diretamente, mas assume que os métodos `take_damage`, `is_alive`, `earn_money` e `add_item` estão implementados corretamente nos objetos `player` e `monster`, e que a lista `monsters` está definida corretamente.
    """
    # Calcula o dano do jogador baseado na arma equipada, se houver
    if player.weapon:
        # Dano do jogador varia entre (dano da arma - 10) e (dano da arma + 10)
        player_damage = random.randint(int(round(max(player.weapon.damage - 10, 0))), int(round(player.weapon.damage + 10)))
    else:
        # Se o jogador não tiver arma, o dano é mínimo
        player_damage = 1

    # Aplica o dano ao monstro
    monster.take_damage(player_damage)

    # Verifica se o monstro foi derrotado
    if not monster.is_alive():
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow(f"Você derrotou {monster.name}!\n")
        print_slow(monster.defeat_message) 
        
        # Ganha experiência e dinheiro
        exp_gained = random.randint(10, 20)
        money_gained = monster.reward
        player.exp += exp_gained
        player.earn_money(money_gained)
        print_slow(f"Você ganhou {exp_gained} de experiência e ${money_gained} de dinheiro.")
        
        # Remove o monstro da lista e verifica se todos foram derrotados
        monsters.remove(monster)
        if not monsters:
            print_slow("\nParabéns! Você venceu todos os monstros acadêmicos e trouxe paz de volta ao campus. Sua coragem e determinação foram inspiradoras. Com a ordem restaurada, os alunos podem agora focar em seus estudos e projetos sem interrupções. Que sua jornada continue cheia de sucesso e aventuras. Até a próxima grande conquista!")
            print_slow("\nComo prêmio você ganhará um chocolate!!!\n")
            return [0, 0, 0]

    # Monstro ataca o jogador
    # Dano do monstro varia entre (dano do monstro - 10) e (dano do monstro + 10)
    monster_damage = random.randint(max(monster.damage - 10, 0), monster.damage + 10)
    
    if player.shield:
        # Calcula o bloqueio do escudo com um range aleatório
        block_amount = random.randint(int(round(max(player.shield.block_amount - 5, 0))), int(round(player.shield.block_amount + 5)))
        # Calcula o dano efetivo recebido pelo jogador
        damage_to_player = max(monster_damage - block_amount, 0)
    else:
        damage_to_player = monster_damage

    # Aplica o dano ao jogador
    if monster.is_alive():
        player.take_damage(damage_to_player)
    
    # Verifica se o jogador foi derrotado
    if not player.is_alive():
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow("Você foi derrotado!")
        print_slow("\nVocê enfrentou muitos desafios e lutou bravamente, mas infelizmente não conseguiu superar todos os obstáculos desta vez. O campus ficou sob a influência dos monstros e os alunos enfrentaram dificuldades. Lembre-se, cada desafio é uma oportunidade para aprender e crescer. Volte mais forte e preparado para a próxima jornada. Até a próxima aventura!")
        print_slow(f"\nTodos lembraram da bravura de {player.name}!!!")
        print_slow("\nComo castigo você deve um chocolate ao Saulo!!!\n")
        return [0, 0, 0]
    
    # Retorna o dano causado pelo jogador, dano do monstro e o bloqueio do escudo
    return [player_damage, monster_damage, block_amount]

def enconter_item(player):
    """
    Escolhe aleatoriamente um item (espada, escudo ou poção) e o adiciona ao inventário do jogador.

    Esta função determina aleatoriamente o tipo de item a ser encontrado, selecionando um item do tipo espada, 
    escudo ou poção com base em probabilidades definidas. 
    O item escolhido é criado usando as configurações específicas para armas, 
    escudos ou poções e é adicionado ao inventário do jogador. 
    A função também exibe uma mensagem informando o jogador sobre o item encontrado e atualiza o status do jogador.

    Parâmetros:
    player (Player): O objeto que representa o jogador, para o qual o item será adicionado ao inventário.

    Comportamento:
    - Escolhe aleatoriamente um tipo de item (espada, escudo ou poção).
    - Seleciona um item específico com base nas probabilidades definidas nas listas de configuração e pesos.
    - Cria uma instância do item selecionado usando as configurações apropriadas.
    - Exibe uma mensagem informando que o item foi encontrado e adicionado ao inventário.
    - Adiciona o item ao inventário do jogador.
    - Mostra o status atualizado do jogador.

    Exceções:
    - Esta função não levanta exceções diretamente, mas assume que as listas de configuração (weapons, shields, potions) e pesos (weight) estão definidos corretamente e que o método `add_item` do objeto `player` está implementado.

    """
    # Escolhe aleatoriamente um tipo de item (espada, escudo ou poção)
    item_type = random.choice(["weapon", "shield", "potion"])
    
    if item_type == "weapon":
        # Escolhe aleatoriamente uma arma com base na probabilidade definida em 'weight'
        config = random.choices(weapons, weights=weight)[0]
        item = Weapon(config[0], config[1], config[2])
    elif item_type == "shield":
        # Escolhe aleatoriamente um escudo com base na probabilidade definida em 'weight'
        config = random.choices(shields, weights=weight)[0]
        item = Shield(config[0], config[1], config[2])
    else:
        # Escolhe aleatoriamente uma poção com base na probabilidade definida em 'weight'
        config = random.choices(potions, weights=weight)[0]
        item = Potion(config[0], config[1], config[2])

    # Exibe a mensagem de que o item foi encontrado
    print_slow("\nVocê encontrou", end='')
    time.sleep(0.5)
    print_slow(" .... ", delay=0.2, end='')
    print_slow(f"{item.name}!\n", delay=0.015)
    time.sleep(0.3)
    
    # Adiciona o item ao inventário do jogador
    player.add_item(item)
    print_slow(f"{item.name} foi adicionado ao seu inventário.\n")
    
    # Mostra o status atualizado do jogador
    player.show_status()

def menu(player):
    """
    Exibe o menu principal do jogo e permite ao jogador escolher ações para realizar.

    Esta função exibe o status atual do jogador e apresenta um menu com opções para equipar itens, 
    vender itens, fazer upgrade em itens, usar poções ou sair do menu.
    Baseado na escolha do jogador,  a função chama a função apropriada para realizar a ação selecionada. 
    Se o jogador optar por sair, o menu será fechado e o jogo continuará. 
    Caso o jogador insira uma opção inválida, uma mensagem de erro será exibida e o menu será apresentado novamente.

    Parâmetros:
    player (Player): O objeto que representa o jogador, contendo informações sobre o status e inventário.

    Comportamento:
    - Limpa a tela e exibe o cabeçalho do menu.
    - Mostra o status atual do jogador.
    - Solicita ao jogador que escolha uma ação a ser tomada.
    - Executa a ação baseada na escolha do jogador:
      - (E)quipar item: Chama a função `equip_item` para permitir que o jogador equipe um item.
      - (V)ender item: Chama a função `sell_item` para permitir que o jogador venda um item.
      - (U)pgrade item: Chama a função `upgrade_item` para permitir que o jogador faça upgrade em um item.
      - (P) usar poção: Chama a função `use_potion` para permitir que o jogador use uma poção.
      - (S)air do Menu: Exibe uma mensagem de saída, limpa a tela e encerra o loop do menu.
    - Se a escolha do jogador for inválida, exibe uma mensagem de erro e aguarda a entrada do jogador para voltar ao menu.

    Exceções:
    - Nenhuma exceção é levantada diretamente por esta função, mas as funções chamadas podem levantar exceções dependendo da implementação delas.

    """
    while True:
        # Limpa a tela antes de mostrar o menu
        os.system('cls' if os.name == 'nt' else 'clear') 
        # Exibe o cabeçalho do menu
        print_slow("\nVocê está no Menu...\n")
        # Mostra o status atual do jogador
        player.show_status()
        # Solicita ao jogador uma ação a ser tomada
        print_slow("\nO que você quer fazer? (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção, (S)air do Menu: ")
        action = input("").lower()
        
        # Executa a ação baseada na escolha do jogador
        if action == 'e':
            equip_item(player)  # Chama a função para equipar um item
        
        elif action == 'v':
            sell_item(player)  # Chama a função para vender um item
        
        elif action == 'u':
            upgrade_item(player)  # Chama a função para fazer upgrade em um item
        
        elif action == 'p':
            use_potion(player)  # Chama a função para usar uma poção

        elif action == 's':
            # Exibe uma mensagem de saída e limpa a tela antes de sair do menu
            print_slow("Saindo do menu.")
            os.system('cls' if os.name == 'nt' else 'clear') 
            break  # Sai do loop e volta ao jogo

        else:
            # Informa ao jogador que a escolha foi inválida e aguarda nova entrada
            print_slow("Escolha inválida. Por favor, escolha (E)quipar item, (V)ender item, (U)pgrade item, (P) usar poção ou (S)air do Menu.")
            print_slow("Pressione 'Enter' para voltar!")
            input("")  # Aguarda o jogador pressionar Enter antes de voltar ao menu

def equip_item(player):
    """
    Permite que o jogador equipe um item de seu inventário.

    Esta função exibe o status atual do jogador e lista todos os itens disponíveis para equipar, excluindo poções. 
    O jogador pode escolher um item para equipar ou voltar ao menu. 
    Se o item selecionado for um item de equipamento (arma ou escudo), ele será equipado e o jogador receberá uma confirmação. 
    Se o item estiver fora do intervalo ou a entrada não for um número válido, uma mensagem de erro será exibida.

    Parâmetros:
    player (Player): O objeto que representa o jogador, contendo informações sobre o inventário, status e itens equipados.

    Comportamento:
    - Limpa a tela e exibe o status atual do jogador.
    - Lista os itens disponíveis para equipar no inventário, excluindo poções.
    - Solicita ao jogador que escolha um item para equipar ou volte ao menu.
    - Se um item válido for selecionado, ele é equipado pelo jogador e uma confirmação é exibida.
    - Se o item estiver equipado e for uma arma ou escudo, ele será corretamente atribuído ao jogador.
    - Caso o índice do item esteja fora do intervalo ou a entrada não seja um número válido, uma mensagem de erro é exibida.
    - Permite ao jogador retornar ao menu pressionando Enter após a ação.

    Exceções:
    - ValueError: Se a entrada do jogador não puder ser convertida para um número válido.

    """
    while True:
        # Limpa a tela antes de mostrar as opções de equipamento
        os.system('cls' if os.name == 'nt' else 'clear') 
        # Exibe o status atual do jogador
        print_slow("Seus status atuais")
        player.show_stats()
        
        # Lista os itens disponíveis para venda
        print_slow("\nEscudos disponíveis para Equipar:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Shield):
                print(f"[{idx + 1}] {item}")
        print_slow("\nArmas disponíveis para Equipar:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Weapon):
                print(f"[{idx + 1}] {item}")

        # Solicita ao jogador que escolha um item para equipar ou volte ao menu
        print_slow("\nDigite o número do item que deseja equipar ou (v) para voltar: ")
        action = input("").lower()
        if action == 'v':
            break  # Sai do loop e volta ao menu
        
        try:
            item_index = int(action) - 1  # Converte a entrada para índice do item
            if 0 <= item_index < len(player.inventory):
                player.equip_item(item_index)  # Tenta equipar o item selecionado
                if not (isinstance(player.inventory[item_index], Potion)):
                    print_slow(f"\nVocê equipou {player.inventory[item_index].name}.")  # Confirmação do equipamento
            else:
                print_slow("Índice do item não encontrado no inventário.")  # Mensagem de erro se o índice estiver fora do intervalo
        except ValueError:
            print_slow("Por favor, insira um número válido.")  # Mensagem de erro se a entrada não for um número
        
        print_slow("\nPressione Enter para voltar ao menu.")  # Mensagem para o jogador pressionar Enter para voltar
        input("")  # Aguarda o jogador pressionar Enter

def sell_item(player):
    """
    Permite que o jogador venda um item de seu inventário e receba dinheiro por isso.

    Esta função exibe o status atual do jogador e lista todos os itens disponíveis para venda. 
    O jogador pode escolher um item para vender ou voltar ao menu. 
    Se o item selecionado estiver equipado, ele será desequipado antes da venda. 
    Após a venda, o item é removido do inventário e o valor da venda é adicionado ao dinheiro do jogador.

    Parâmetros:
    player (Player): O objeto que representa o jogador, contendo informações sobre o inventário, dinheiro e status atual.

    Comportamento:
    - Limpa a tela e exibe o status atual do jogador.
    - Lista os itens disponíveis para venda no inventário.
    - Solicita ao jogador que escolha um item para vender ou volte ao menu.
    - Se um item for selecionado para venda, o item é removido do inventário e o valor correspondente é adicionado ao dinheiro do jogador.
    - Se o item estiver equipado (como uma arma ou escudo), ele é desequipado antes da venda.
    - Caso o índice do item esteja fora do intervalo ou a entrada não seja um número válido, uma mensagem de erro é exibida.
    - Permite ao jogador retornar ao menu pressionando Enter após a ação.

    Exceções:
    - ValueError: Se a entrada do jogador não puder ser convertida para um número válido.

    """
    while True:
        # Limpa a tela antes de mostrar as opções de venda
        os.system('cls' if os.name == 'nt' else 'clear') 

        # Exibe o status atual do jogador
        print_slow("Seus status atuais")
        player.show_stats()

        # Lista os itens disponíveis para venda
        print_slow("\nEscudos disponíveis para Vender:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Shield):
                print(f"[{idx + 1}] {item}")
        print_slow("\nArmas disponíveis para Vender:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Weapon):
                print(f"[{idx + 1}] {item}")
        print_slow("\nPoções disponíveis para Vender:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Potion):
                print(f"[{idx + 1}] {item}")

        # Solicita ao jogador que escolha um item para vender ou volte ao menu
        print_slow("\nDigite o número do item que deseja vender ou (v) para voltar: ")
        action = input("").lower()
        if action == 'v':
            break  # Sai do loop e volta ao menu
        
        try:
            item_index = int(action) - 1  # Converte a entrada para índice do item
            if 0 <= item_index < len(player.inventory):
                item_to_sell = player.inventory[item_index]
                
                # Verifica se o item vendido está equipado e desequipa se necessário
                if player.weapon == item_to_sell:
                    player.weapon = None
                if player.shield == item_to_sell:
                    player.shield = None

                # Remove o item do inventário e adiciona seu valor ao dinheiro do jogador
                player.inventory.pop(item_index)
                player.earn_money(item_to_sell.value)
                print_slow(f"\nVocê vendeu {item_to_sell.name} por ${item_to_sell.value}.")  # Confirmação da venda
            else:
                print_slow("Índice do item não encontrado no inventário.")  # Mensagem de erro se o índice estiver fora do intervalo
        except ValueError:
            print_slow("Por favor, insira um número válido.")  # Mensagem de erro se a entrada não for um número
        
        print_slow("\nPressione Enter para voltar ao menu.")  # Mensagem para o jogador pressionar Enter para voltar
        input("")  # Aguarda o jogador pressionar Enter

def upgrade_item(player):
    """
    Permite que o jogador use uma poção de seu inventário para curar a saúde.

    Esta função exibe o status atual do jogador e as poções disponíveis no inventário. 
    O jogador pode escolher uma poção para usar ou voltar ao menu. Se uma poção for usada, 
    a saúde do jogador será aumentada pelo valor da poção, respeitando o limite máximo de 100. 
    O excesso de cura será desperdiçado. Após o uso da poção, ela será removida do inventário.

    Parâmetros:
    player (Player): O objeto que representa o jogador, contendo informações sobre o inventário, saúde e status atual.

    Comportamento:
    - Limpa a tela e exibe uma mensagem sobre o limite de HP.
    - Mostra o status atual do jogador.
    - Lista as poções disponíveis para uso.
    - Solicita ao jogador que escolha uma poção ou volte ao menu.
    - Se uma poção for selecionada, a saúde do jogador será atualizada e a poção será removida do inventário.
    - Caso o item selecionado não seja uma poção ou o índice esteja fora do intervalo, exibe uma mensagem de erro.
    - Permite ao jogador retornar ao menu pressionando Enter após a ação.

    Exceções:
    - ValueError: Se a entrada do jogador não puder ser convertida para um número válido.

    """
    while True:
        # Limpa a tela antes de mostrar as opções de upgrade
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        # Exibe o status atual do jogador
        print_slow("Seus status atuais")
        player.show_stats()

        # Lista os itens disponíveis para venda
        print_slow("\nEscudos disponíveis para Upgrade:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Shield):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Bloqueio atual: {item.block_amount:.2f}, Bloqueio após upgrade: {item.calculate_next_block():.2f}")
        print_slow("\nArmas disponíveis para Upgrade:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Weapon):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Dano atual: {item.damage:.2f}, Dano após upgrade: {item.calculate_next_damage():.2f}")
        print_slow("\nPoções disponíveis para Upgrade:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Potion):
                print(f"[{idx + 1}] {item.name} - Custo: ${item.value * 1.5:.2f}, Nível atual: {item.level}, Cura atual: {item.heal_amount:.2f}, Cura após upgrade: {item.calculate_next_heal():.2f}")
        
        # Solicita ao jogador que escolha um item para melhorar ou volte ao menu
        print_slow("\nDigite o número do item que deseja melhorar ou (v) para voltar: ")
        action = input("").lower()
        if action == 'v':
            break  # Sai do loop e volta ao menu
        
        try:
            item_index = int(action) - 1  # Converte a entrada para índice do item
            if 0 <= item_index < len(player.inventory):
                item_to_upgrade = player.inventory[item_index]
                # Verifique se o jogador tem dinheiro suficiente para o upgrade
                upgrade_cost = item_to_upgrade.value * 1.5
                if player.money >= upgrade_cost:
                    item_to_upgrade.upgrade()  # Melhora o item
                    player.earn_money(-upgrade_cost)  # Deduz o custo do upgrade do dinheiro do jogador
                    print_slow(f"\nVocê melhorou {item_to_upgrade.name} para nível {item_to_upgrade.level}.")  # Confirmação do upgrade
                else:
                    print_slow("Dinheiro insuficiente para o upgrade.")  # Mensagem de erro se o jogador não tiver dinheiro suficiente
            else:
                print_slow("Índice do item não encontrado no inventário.")  # Mensagem de erro se o índice estiver fora do intervalo
        except ValueError:
            print_slow("Por favor, insira um número válido.")  # Mensagem de erro se a entrada não for um número
        
        print_slow("\nPressione Enter para voltar ao menu.")  # Mensagem para o jogador pressionar Enter para voltar
        input("")  # Aguarda o jogador pressionar Enter

def use_potion(player):
    while True:
        # Limpa a tela e informa ao jogador sobre o limite de HP
        os.system('cls' if os.name == 'nt' else 'clear') 
        print_slow("Lembre-se que o hp máx é 100, então o excedente de cura será desperdiçado!!!\n")
        
        # Exibe o status atual do jogador
        print_slow("Seus status atuais")
        player.show_stats()
        
        # Lista as poções disponíveis para uso
        print_slow("\nPoções disponíveis para uso:")
        for idx, item in enumerate(player.inventory):
            if isinstance(item, Potion):
                print(f"[{idx + 1}] {item}")

        # Solicita ao jogador que escolha uma poção para usar ou volte ao menu
        print_slow("\nDigite o número da poção que deseja usar ou (v) para voltar: ")
        action = input("").lower()
        if action == 'v':
            break  # Sai do loop e volta ao menu
        
        try:
            item_index = int(action) - 1  # Converte a entrada para índice do item
            if 0 <= item_index < len(player.inventory):
                potion_to_use = player.inventory[item_index]
                if isinstance(potion_to_use, Potion):
                    # Atualiza o HP do jogador com o valor da poção, respeitando o limite máximo de 100
                    player.hp = min(100.0, round(player.hp + potion_to_use.heal_amount, 2))
                    player.show_status()  # Mostra o status atualizado após usar a poção
                    print_slow(f"\nVocê usou {potion_to_use.name}.")
                    player.inventory.pop(item_index)  # Remove a poção usada do inventário
                else:
                    print_slow("O item selecionado não é uma poção.")
            else:
                print_slow("Índice do item não encontrado no inventário.")
        except ValueError:
            print_slow("Por favor, insira um número válido.")
        
        print_slow("\nPressione Enter para voltar ao menu.")  # Mensagem para o jogador pressionar Enter para voltar
        input("")  # Aguarda o jogador pressionar Enter
