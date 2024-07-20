from player import Player
from items import Weapon, Potion, Shield
from functions import explore, inventory

def main():
    print("A Jornada Acadêmica: Desafios do Campus!")
    
    name = input("Digite seu nome nobre guerreiro: ")

    print(f"{name}, você é um estudante da EMAP, conhecida por seus desafios acadêmicos e atividades extracurriculares intensas. Recentemente, estranhas ocorrências começaram a afetar o campus: monstros acadêmicos surgem nos corredores, provas se tornam mais difíceis e até mesmo professores parecem estar agindo de maneira peculiar. Você, como um aluno destemido, decide enfrentar esses desafios e restaurar a ordem no campus.")

    player = Player(name)

    # Adicionando alguns itens ao inventário do jogador
    player.add_item(Weapon("Espada do Destino", 150, 25))
    player.add_item(Potion("Poção de Cura Maior", 50, 20))
    player.add_item(Shield("Escudo de Ferro", 100, 10))

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
