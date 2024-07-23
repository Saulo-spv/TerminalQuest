"""
Módulo Principal

Este módulo contém a função principal que gerencia o fluxo do jogo, incluindo a introdução, 
o menu de opções e o loop principal do jogo.

Funções:
- `main()`: Função principal que executa o fluxo do jogo.

"""

from player import Player
from functions import explore, menu, tutorial, print_slow
from enemies import monsters
import os, random, time

def main():
    """
    Função principal que executa o fluxo do jogo.

    Esta função é responsável por:
    - Definir a semente aleatória com `random.seed(time.time())` para garantir que as operações aleatórias sejam baseadas no tempo atual.
    - Limpar a tela usando `os.system('cls' if os.name == 'nt' else 'clear')` para diferentes sistemas operacionais.
    - Exibir mensagens de introdução e instruções do jogo utilizando a função `print_slow`, que imprime texto lentamente para criar uma experiência mais envolvente.
    - Solicitar o nome do jogador e criar uma nova instância do jogador com a classe `Player`.
    - Mostrar uma mensagem de boas-vindas e instruir o jogador a apertar 'Enter' para começar o jogo.
    - Chamar a função `tutorial` para fornecer um tutorial inicial ao jogador.
    - Executar um loop onde o jogador pode escolher entre explorar, acessar o menu ou sair do jogo.
    - Processar a escolha do jogador e chamar as funções apropriadas (`explore`, `menu`) ou confirmar a saída do jogo.
    - Confirmar a saída do jogo e, se o jogador optar por sair, exibir uma mensagem de agradecimento e terminar o jogo.

    Dependências:
    - `os`: Para limpar a tela do terminal.
    - `random`: Para definir a semente aleatória.
    - `time`: Para obter o tempo atual e definir a semente aleatória.
    - `Player`: Para criar uma instância de jogador.
    - `explore`: Função para explorar o jogo.
    - `menu`: Função para exibir o menu de opções.
    - `tutorial`: Função para exibir o tutorial inicial.
    - `print_slow`: Função para exibir texto lentamente.
    - `monsters`: Lista de monstros disponíveis no jogo.
    """

    # Definir a semente aleatória com base no tempo atual
    random.seed(time.time())

    # Limpar a tela dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear') 

    # Mensagens de introdução com uma função para exibir texto lentamente
    print_slow("Bem-vindo a 'A Jornada Acadêmica: Desafios do Campus!'")
    print_slow("\nVocê está prestes a embarcar em uma aventura emocionante pelos corredores da EMAP, uma universidade repleta de desafios e monstros acadêmicos.")
    print_slow("Neste jogo, você assumirá o papel de um estudante destemido que deve enfrentar diversas criaturas relacionadas a estresse acadêmico e desorganização.")
    print_slow("\nAqui estão algumas das mecânicas principais do jogo:")
    print_slow("1. **Exploração**: Caminhe pelos corredores do campus para encontrar monstros e novos itens.")
    print_slow("2. **Combate**: Lute contra monstros acadêmicos usando armas e escudos que você encontra ou adquire.")
    print_slow("3. **Inventário**: Gerencie itens como armas, escudos e poções que você coleta para melhorar suas habilidades e se curar.")
    print_slow("4. **Progressão**: Ganhe experiência e dinheiro ao derrotar monstros. Use esses recursos para aprimorar seu personagem e enfrentar adversários mais poderosos.")
    print_slow("5. **Finalização**: Para vencer o jogo, você deve derrotar todos os 7 monstros acadêmicos que assombram o campus.")

    # Solicitar o nome do jogador
    print_slow("\nDigite seu nome, nobre estudante: ")
    name = input("")
    player = Player(name)  # Criar uma nova instância do jogador com o nome fornecido

    # Mensagem de boas-vindas e início da jornada
    print_slow(f"\nSeja bem-vindo, {player.name}! Sua jornada começa agora. Prepare-se para enfrentar os desafios e restaurar a ordem no campus!")
    print_slow("Aperte 'Enter' para começar!")
    input("")

    # Mostrar o tutorial inicial
    tutorial(player)

    # Loop principal do jogo
    while player.is_alive() and monsters:
        # Solicitar a ação do jogador
        print_slow("\nO que você quer fazer? (E)xplorar, (M)enu, (S)air: ")
        action = input("").lower()
        if action == 'e':
            explore(player)  # Chamar a função de exploração
        elif action == 'm':
            menu(player)  # Mostrar o menu de opções
        elif action == 's':
            # Confirmar saída do jogo
            os.system('cls' if os.name == 'nt' else 'clear') 
            print_slow("Você está prestes a sair do jogo. Atenção: Se você sair agora, todos os progressos e conquistas atuais serão perdidos, e o campus ficará à mercê dos monstros novamente. Tem certeza de que deseja encerrar sua jornada?")
            confirm_exit = input("Digite 'sim' para confirmar ou 'não' para voltar: ").lower()
            if confirm_exit == 'sim':
                print_slow("Obrigado por jogar! Esperamos vê-lo novamente em futuras aventuras. Até mais!")
                break
            else:
                print_slow("Você decidiu continuar. Vamos lá, a aventura ainda não acabou!")
        else:
            print_slow("Por favor, escolha (E)xplorar, (M)enu ou (S)air.")

if __name__ == "__main__":
    main()
