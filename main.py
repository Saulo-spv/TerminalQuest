from player import Player
from items import Weapon, Potion, Shield
from functions import explore, menu, tutorial
from enemies import monsters
import os

def main():

    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Bem-vindo a 'A Jornada Acadêmica: Desafios do Campus!'")
    print("\nVocê está prestes a embarcar em uma aventura emocionante pelos corredores da EMAP, uma universidade repleta de desafios e monstros acadêmicos.")
    print("Neste jogo, você assumirá o papel de um estudante destemido que deve enfrentar diversas criaturas relacionadas a estresse acadêmico e desorganização.")
    print("\nAqui estão algumas das mecânicas principais do jogo:")
    print("1. **Exploração**: Caminhe pelos corredores do campus para encontrar monstros e novos itens.")
    print("2. **Combate**: Lute contra monstros acadêmicos usando armas e escudos que você encontra ou adquire.")
    print("3. **Inventário**: Gerencie itens como armas, escudos e poções que você coleta para melhorar suas habilidades e se curar.")
    print("4. **Progressão**: Ganhe experiência e dinheiro ao derrotar monstros. Use esses recursos para aprimorar seu personagem e enfrentar adversários mais poderosos.")
    print("5. **Finalização**: Para vencer o jogo, você deve derrotar todos os 7 monstros acadêmicos que assombram o campus.")

    name = input("\nDigite seu nome, nobre estudante: ")
    player = Player(name)

    print(f"\nSeja bem-vindo, {player.name}! Sua jornada começa agora. Prepare-se para enfrentar os desafios e restaurar a ordem no campus!")

    tutorial(player)

    while player.is_alive() and monsters:
        action = input("\nO que você quer fazer? (E)xplorar, (M)enu, (S)air: ").lower()
        if action == 'e':
            explore(player)
        elif action == 'm':
            menu(player)
        elif action == 's':
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("Você está prestes a sair do jogo. Atenção: Se você sair agora, todos os progressos e conquistas atuais serão perdidos, e o campus ficará à mercê dos monstros novamente. Tem certeza de que deseja encerrar sua jornada?")
            confirm_exit = input("Digite 'sim' para confirmar ou 'não' para voltar: ").lower()
            if confirm_exit == 'sim':
                print("Obrigado por jogar! Esperamos vê-lo novamente em futuras aventuras. Até mais!")
                break
            else:
                print("Você decidiu continuar. Vamos lá, a aventura ainda não acabou!")
        else:
            print("Por favor, escolha (E)xplorar, (I)nventário ou (Q)uit.")

if __name__ == "__main__":
    main()
