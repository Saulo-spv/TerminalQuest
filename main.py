from player import Player
from items import Weapon, Potion, Shield
from functions import explore, menu, tutorial
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("A Jornada Acadêmica: Desafios do Campus!")
    
    name = input("Digite seu nome nobre guerreiro: ")
    player = Player(name)

    tutorial(player)

    while player.is_alive():
        action = input("\nO que você quer fazer? (E)xplorar, (M)enu, (S)air: ").lower()
        if action == 'e':
            explore(player)
        elif action == 'm':
            menu(player)
        elif action == 's':
            print("Obrigado por jogar!")
            break
        else:
            print("Por favor, escolha (E)xplorar, (I)nventário ou (Q)uit.")

if __name__ == "__main__":
    main()
