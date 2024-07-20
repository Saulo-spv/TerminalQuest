from player import Player
from items import Weapon, Potion, Shield
from functions import explore, inventory, tutorial

def main():
    print("A Jornada Acadêmica: Desafios do Campus!")
    
    name = input("Digite seu nome nobre guerreiro: ")

    print(f"{name}, você é um estudante da EMAP, conhecida por seus desafios acadêmicos e atividades extracurriculares intensas. Recentemente, estranhas ocorrências começaram a afetar o campus: monstros acadêmicos surgem nos corredores, provas se tornam mais difíceis e até mesmo professores parecem estar agindo de maneira peculiar. Você, como um aluno destemido, decide enfrentar esses desafios e restaurar a ordem no campus.")

    player = Player(name)

    tutorial(player)

    while player.is_alive():
        action = input("\nO que você quer fazer? (E)xplorar, (M)enu, (S)air: ").lower()
        if action == 'e':
            explore(player)
        elif action == 'm':
            inventory(player)
        elif action == 's':
            print("Obrigado por jogar!")
            break
        else:
            print("Por favor, escolha (E)xplorar, (I)nventário ou (Q)uit.")

if __name__ == "__main__":
    main()
