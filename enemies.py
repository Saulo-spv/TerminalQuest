class Enemy:
    def __init__(self, name, description, hp, damage, weakness, special_attack):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.weakness = weakness
        self.special_attack = special_attack

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
    Enemy("Monstro da Procrastinação", "Um ser nebuloso e enganador que adia tarefas e compromissos. Ele causa distrações e tenta desviar a atenção do jogador.", 7, 1, "Motivação", "Desvio de Atenção"),
    Enemy("Espírito da Ansiedade", "Uma entidade perturbadora que causa nervosismo e pânico. Aumenta a dificuldade dos desafios enfrentados pelo jogador.", 8, 2, "Calma e Planejamento", "Crise de Ansiedade"),
    #Enemy("Monstro do Trabalho de Casa", "Uma criatura que surge de pilhas intermináveis de tarefas e trabalhos escolares. Pode atacar com tarefas desafiadoras e demoradas.", 90, 25, "Organização e Tempo", "Sobrecarregar"),
    #Enemy("Fantasma da Fadiga", "Um espectro que exaure a energia dos alunos com seu cansaço constante. Reduz a eficácia dos ataques do jogador.", 60, 10, "Energia e Descanso", "Exaustão"),
    #Enemy("Demônio da Dúvida", "Uma entidade que se alimenta das inseguranças e dúvidas dos alunos. Cria incertezas e dificuldade em tomar decisões rápidas.", 75, 18, "Confiança", "Dúvida Paralizante"),
    #Enemy("Monstro da Desorganização", "Uma criatura caótica que faz com que itens e tarefas fiquem desordenados e difíceis de encontrar.", 85, 22, "Planejamento e Organização", "Confusão de Itens"),
    #Enemy("Ser do Estresse", "Uma figura opressiva que aumenta o nível de estresse do jogador, afetando suas habilidades e desempenho.", 95, 30, "Relaxamento e Técnicas de Alívio", "Pico de Estresse")
]
