class Enemy:
    def __init__(self, name, description, hp, damage, weakness, special_attack, reward, defeat_message):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.weakness = weakness
        self.special_attack = special_attack
        self.reward = reward
        self.defeat_message = defeat_message

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"Nome: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Dano: {self.damage}")

# Definindo os monstros
monsters = [
    Enemy("Monstro da Procrastinação", "Um ser nebuloso e enganador que adia tarefas e compromissos. Ele causa distrações e tenta desviar a atenção do jogador.", 30, 10, "Motivação", "Desvio de Atenção", 10, "Você conseguiu vencer a procrastinação! Agora, siga em frente sem distrações."),
    Enemy("Espírito da Ansiedade", "Uma entidade perturbadora que causa nervosismo e pânico. Aumenta a dificuldade dos desafios enfrentados pelo jogador.", 40, 25, "Calma e Planejamento", "Crise de Ansiedade", 20, "Com a sua calma e planejamento, você derrotou a ansiedade! O caminho está mais tranquilo agora."),
    Enemy("Monstro do Trabalho de Casa", "Uma criatura que surge de pilhas intermináveis de tarefas e trabalhos escolares. Pode atacar com tarefas desafiadoras e demoradas.", 70, 30, "Organização e Tempo", "Sobrecarregar", 30, "Você venceu a sobrecarga de tarefas! Agora é hora de organizar melhor seu tempo."),
    Enemy("Fantasma da Fadiga", "Um espectro que exaure a energia dos alunos com seu cansaço constante. Reduz a eficácia dos ataques do jogador.", 60, 35, "Energia e Descanso", "Exaustão", 40, "A fadiga foi superada! Sinta a energia retornando e continue sua jornada."),
    Enemy("Demônio da Dúvida", "Uma entidade que se alimenta das inseguranças e dúvidas dos alunos. Cria incertezas e dificuldade em tomar decisões rápidas.", 90, 40, "Confiança", "Dúvida Paralizante", 60, "Você derrotou a dúvida! Agora, suas decisões são mais claras e confiantes."),
    Enemy("Monstro da Desorganização", "Uma criatura caótica que faz com que itens e tarefas fiquem desordenados e difíceis de encontrar.", 100, 45, "Planejamento e Organização", "Confusão de Itens", 80, "A desorganização foi vencida! O campus está mais organizado e fácil de navegar."),
    Enemy("Ser do Estresse", "Uma figura opressiva que aumenta o nível de estresse do jogador, afetando suas habilidades e desempenho.", 120, 50, "Relaxamento e Técnicas de Alívio", "Pico de Estresse", 100, "O estresse foi superado! Você se sente mais relaxado e preparado para os desafios futuros.")
]
