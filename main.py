from player import Player
from functions import explore, menu, tutorial, print_slow
from enemies import monsters
import os, random, time

def main():

    # Definir a semente aqui
    random.seed(time.time())

    os.system('cls' if os.name == 'nt' else 'clear') 
    print_slow("Bem-vindo a 'A Jornada Acadêmica: Desafios do Campus!'")
    print_slow("\nVocê está prestes a embarcar em uma aventura emocionante pelos corredores da EMAP, uma universidade repleta de desafios e monstros acadêmicos.")
    print_slow("Neste jogo, você assumirá o papel de um estudante destemido que deve enfrentar diversas criaturas relacionadas a estresse acadêmico e desorganização.")
    print_slow("\nAqui estão algumas das mecânicas principais do jogo:")
    print_slow("1. **Exploração**: Caminhe pelos corredores do campus para encontrar monstros e novos itens.")
    print_slow("2. **Combate**: Lute contra monstros acadêmicos usando armas e escudos que você encontra ou adquire.")
    print_slow("3. **Inventário**: Gerencie itens como armas, escudos e poções que você coleta para melhorar suas habilidades e se curar.")
    print_slow("4. **Progressão**: Ganhe experiência e dinheiro ao derrotar monstros. Use esses recursos para aprimorar seu personagem e enfrentar adversários mais poderosos.")
    print_slow("5. **Finalização**: Para vencer o jogo, você deve derrotar todos os 7 monstros acadêmicos que assombram o campus.")

    print_slow("\nDigite seu nome, nobre estudante: ")
    name = input("")
    player = Player(name)

    print_slow(f"\nSeja bem-vindo, {player.name}! Sua jornada começa agora. Prepare-se para enfrentar os desafios e restaurar a ordem no campus!")
    print_slow("Aperte 'Enter' para começar!")
    input("")

    tutorial(player)

    while player.is_alive() and monsters:
        print_slow("\nO que você quer fazer? (E)xplorar, (M)enu, (S)air: ")
        action = input("").lower()
        if action == 'e':
            explore(player)
        elif action == 'm':
            menu(player)
        elif action == 's':
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
