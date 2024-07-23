# RPG de Texto - Jogo de Aventura

Bem-vindo ao **RPG de Texto**, um emocionante jogo de aventura baseado em texto! Embarque em uma jornada desafiadora onde você enfrentará monstros, coletará itens mágicos e lutará para alcançar seu objetivo final. Este projeto foi desenvolvido em Python e apresenta um sistema de itens detalhado e um enredo envolvente ambientado em um ambiente acadêmico fictício.

## Enredo

Você está em um mundo acadêmico repleto de desafios e criaturas místicas que representam as dificuldades da vida universitária. Seu objetivo é derrotar todos os 7 monstros que representam diferentes aspectos do estresse acadêmico. Cada monstro oferece um desafio único e requer estratégias diferentes para ser vencido. Prepare-se para enfrentar monstros como o **Demônio da Dúvida** e o **Fantasma da Fadiga**, e colete itens poderosos para ajudá-lo em sua jornada.

## Objetivo do Jogo

O objetivo principal é derrotar todos os 7 monstros do jogo. Cada monstro possui características únicas que influenciam a batalha, e você precisará gerenciar seu equipamento e usar estratégias apropriadas para vencê-los.

## Mecânicas do Jogo

### Itens

Você pode encontrar e usar três tipos principais de itens:

- **Armas**: Aumentam o dano causado aos inimigos. Cada arma pode ser aprimorada para aumentar seu dano.
- **Escudos**: Reduzem o dano recebido dos inimigos. Cada escudo pode ser aprimorado para melhorar sua capacidade de bloqueio.
- **Poções**: Curam o jogador. Cada poção pode ser aprimorada para aumentar a quantidade de cura fornecida.

### Atualizações de Itens

Todos os itens têm níveis que podem ser aumentados. A cada atualização, o valor do item, o dano, o bloqueio ou a cura é incrementado. O custo para atualizar um item também aumenta a cada nível.

### Batalhas

Durante o jogo, você enfrentará monstros com diferentes níveis de HP (vida) e dano. As batalhas são baseadas em texto, onde você escolhe suas ações e usa seu equipamento estrategicamente para vencer os inimigos.

### Sistema de Itens

Os itens são gerenciados com base em listas predefinidas que contêm armas, escudos e poções. Cada item tem um nome, valor e propriedades específicas (dano, bloqueio ou cura). Além disso, há uma lista de pesos que determina a probabilidade de encontrar diferentes tipos de itens durante o jogo.

## Itens Disponíveis

Aqui estão os itens que você pode encontrar e utilizar no jogo, eles estão distribuidos em classes Comuns, Raros e Lendários:

### Armas

1. **Espada de Treinamento**
   - **Valor**: R$50
   - **Dano**: 12

2. **Espada do Guerreiro**
   - **Valor**: R$100
   - **Dano**: 20

3. **Lâmina da Tempestade**
   - **Valor**: R$200
   - **Dano**: 35

### Escudos

1. **Escudo de Madeira**
   - **Valor**: R$30
   - **Bloqueio**: 5

2. **Escudo de Ferro**
   - **Valor**: R$70
   - **Bloqueio**: 8

3. **Escudo de Aço**
   - **Valor**: R$150
   - **Bloqueio**: 15

### Poções

1. **Poção de Cura Leve**
   - **Valor**: R$20
   - **Cura**: 20

2. **Poção de Cura Média**
   - **Valor**: R$50
   - **Cura**: 30

3. **Poção de Cura Forte**
   - **Valor**: R$100
   - **Cura**: 40

### Pesos para Itens

Os pesos indicam a probabilidade relativa de encontrar cada tipo de item:

- **Lendário**: 60%
- **Raro**: 30%
- **Comum**: 10%

## Início Rápido

Para começar a jogar, siga estas etapas:

1. **Clone o Repositório**:
```bash
https://github.com/Saulo-spv/TerminalQuest.git
```

2. **Execute o Jogo**:
```bash
python main.py
```

Siga as instruções no terminal para explorar o mundo, encontrar itens e enfrentar monstros.

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o jogo ou adicionar novos recursos, sinta-se à vontade para enviar um pull request.
