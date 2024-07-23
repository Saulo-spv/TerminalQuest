"""
Módulo `enemies`

Este módulo define a classe `Enemy` e uma lista de inimigos que representam desafios no jogo.

A classe `Enemy` é usada para criar inimigos com propriedades específicas, como pontos de vida (HP), dano, fraqueza, 
ataque especial, recompensa e mensagem de derrota.

Classes:
- `Enemy`: Representa um inimigo no jogo.

Atributos do módulo:
- `monsters` (list): Uma lista de instâncias da classe `Enemy`, representando inimigos com características específicas que o jogador pode enfrentar.

Detalhes das Classes:
- `Enemy`: 
    - Inicializa com um nome, descrição, pontos de vida iniciais, dano, fraqueza, ataque especial, recompensa e mensagem de derrota.
    - Métodos:
        - `take_damage(damage)`: Reduz os pontos de vida do inimigo com base no dano recebido.
        - `is_alive()`: Verifica se o inimigo ainda está vivo (HP > 0).
        - `show_status()`: Exibe o status atual do inimigo.
        - `restore_hp()`: Restaura os pontos de vida do inimigo para o valor inicial.

Atributos do Módulo:
- `monsters`:
    - Uma lista que contém várias instâncias da classe `Enemy`, cada uma representando um inimigo específico com características detalhadas.

Exemplos de Inimigos:
- `Monstro da Procrastinação`: Um inimigo com HP 30, dano 10, fraqueza "Motivação", ataque especial "Desvio de Atenção", e recompensa 10 moedas.
- `Espírito da Ansiedade`: Um inimigo com HP 40, dano 25, fraqueza "Calma e Planejamento", ataque especial "Crise de Ansiedade", e recompensa 20 moedas.
- `Monstro do Trabalho de Casa`: Um inimigo com HP 70, dano 30, fraqueza "Organização e Tempo", ataque especial "Sobrecarregar", e recompensa 30 moedas.
- `Fantasma da Fadiga`: Um inimigo com HP 60, dano 35, fraqueza "Energia e Descanso", ataque especial "Exaustão", e recompensa 40 moedas.
- `Demônio da Dúvida`: Um inimigo com HP 90, dano 40, fraqueza "Confiança", ataque especial "Dúvida Paralizante", e recompensa 60 moedas.
- `Monstro da Desorganização`: Um inimigo com HP 100, dano 45, fraqueza "Planejamento e Organização", ataque especial "Confusão de Itens", e recompensa 80 moedas.
- `Ser do Estresse`: Um inimigo com HP 120, dano 50, fraqueza "Relaxamento e Técnicas de Alívio", ataque especial "Pico de Estresse", e recompensa 100 moedas.
"""

class Enemy:
    """
    Representa um inimigo no jogo.

    Atributos:
    name (str): O nome do inimigo.
    description (str): A descrição do inimigo.
    initial_hp (int): Pontos de vida iniciais do inimigo.
    hp (int): Pontos de vida atuais do inimigo.
    damage (int): Dano causado pelo inimigo.
    weakness (str): Fraqueza do inimigo.
    special_attack (str): Ataque especial do inimigo.
    reward (int): Recompensa dada ao vencer o inimigo.
    defeat_message (str): Mensagem exibida ao derrotar o inimigo.

    Métodos:
    take_damage(damage): Reduz os pontos de vida do inimigo com base no dano recebido.
    is_alive(): Verifica se o inimigo ainda está vivo (HP > 0).
    show_status(): Exibe o status do inimigo.
    restore_hp(): Restaura os pontos de vida do inimigo para o valor inicial.
    """
    def __init__(self, name, description, hp, damage, weakness, special_attack, reward, defeat_message):
        """
        Inicializa as propriedades do inimigo.

        Parâmetros:
        name (str): O nome do inimigo.
        description (str): A descrição do inimigo.
        hp (int): Pontos de vida iniciais do inimigo.
        damage (int): Dano causado pelo inimigo.
        weakness (str): Fraqueza do inimigo.
        special_attack (str): Ataque especial do inimigo.
        reward (int): Recompensa dada ao vencer o inimigo.
        defeat_message (str): Mensagem exibida ao derrotar o inimigo.
        """
        self.name = name  # Nome do inimigo
        self.description = description  # Descrição do inimigo
        self.initial_hp = hp  # Pontos de vida iniciais do inimigo
        self.hp = hp  # Pontos de vida atuais do inimigo
        self.damage = damage  # Dano causado pelo inimigo
        self.weakness = weakness  # Fraqueza do inimigo
        self.special_attack = special_attack  # Ataque especial do inimigo
        self.reward = reward  # Recompensa dada ao vencer o inimigo
        self.defeat_message = defeat_message  # Mensagem exibida ao derrotar o inimigo

    def take_damage(self, damage):
        """
        Reduz os pontos de vida do inimigo com base no dano recebido.

        Parâmetros:
        damage (int): A quantidade de dano a ser aplicada.

        Comportamento:
        - Reduz o HP do inimigo pelo valor de `damage`.
        - Garante que o HP não fique abaixo de 0.
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # Garante que a vida não fique negativa

    def is_alive(self):
        """
        Verifica se o inimigo ainda está vivo (HP > 0).

        Retorna:
        bool: True se o inimigo estiver vivo, False caso contrário.
        """
        return self.hp > 0

    def show_status(self):
        """
        Exibe o status atual do inimigo.

        Comportamento:
        - Imprime o nome, HP e dano do inimigo.
        """
        print(f"Nome: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Dano: {self.damage}")

    def restore_hp(self):
        """
        Restaura os pontos de vida do inimigo para o valor inicial.

        Comportamento:
        - Define o HP atual do inimigo para o valor de `initial_hp`.
        """
        self.hp = self.initial_hp


# Definindo os monstros com suas características específicas
monsters = [
    Enemy("Monstro da Procrastinação", 
          "Um ser nebuloso e enganador que adia tarefas e compromissos. Ele causa distrações e tenta desviar a atenção do jogador.", 
          30, 10, "Motivação", "Desvio de Atenção", 10, 
          "Você conseguiu vencer a procrastinação! Agora, siga em frente sem distrações.\n"),
    
    Enemy("Espírito da Ansiedade", 
          "Uma entidade perturbadora que causa nervosismo e pânico. Aumenta a dificuldade dos desafios enfrentados pelo jogador.", 
          40, 25, "Calma e Planejamento", "Crise de Ansiedade", 20, 
          "Com a sua calma e planejamento, você derrotou a ansiedade! O caminho está mais tranquilo agora.\n"),
    
    Enemy("Monstro do Trabalho de Casa", 
          "Uma criatura que surge de pilhas intermináveis de tarefas e trabalhos escolares. Pode atacar com tarefas desafiadoras e demoradas.", 
          70, 30, "Organização e Tempo", "Sobrecarregar", 30, 
          "Você venceu a sobrecarga de tarefas! Agora é hora de organizar melhor seu tempo.\n"),
    
    Enemy("Fantasma da Fadiga", 
          "Um espectro que exaure a energia dos alunos com seu cansaço constante. Reduz a eficácia dos ataques do jogador.", 
          60, 35, "Energia e Descanso", "Exaustão", 40, 
          "A fadiga foi superada! Sinta a energia retornando e continue sua jornada.\n"),
    
    Enemy("Demônio da Dúvida", 
          "Uma entidade que se alimenta das inseguranças e dúvidas dos alunos. Cria incertezas e dificuldade em tomar decisões rápidas.", 
          90, 40, "Confiança", "Dúvida Paralizante", 60, 
          "Você derrotou a dúvida! Agora, suas decisões são mais claras e confiantes.\n"),
    
    Enemy("Monstro da Desorganização", 
          "Uma criatura caótica que faz com que itens e tarefas fiquem desordenados e difíceis de encontrar.", 
          100, 45, "Planejamento e Organização", "Confusão de Itens", 80, 
          "A desorganização foi vencida! O campus está mais organizado e fácil de navegar.\n"),
    
    Enemy("Ser do Estresse", 
          "Uma figura opressiva que aumenta o nível de estresse do jogador, afetando suas habilidades e desempenho.", 
          120, 50, "Relaxamento e Técnicas de Alívio", "Pico de Estresse", 100, 
          "O estresse foi superado! Você se sente mais relaxado e preparado para os desafios futuros.\n")
]
