# Jogo da forca em linguagem Python

#Imports:

import random
from os import system, name

#Funções:

# Função para limpar a tela a cada execução
def limpaTela():
    
    # Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')

# Função que dá início ao jogo;
def jogo():
    limpaTela()

    print("\nBem vindo ao jogo da forca!!!")
    print("Adivinhe a palavra abaixo: \n")

    # Lista de palavras para o jogo
    carros_japoneses = [
        "civic", "corolla", "lancer", "skyline", "supra",  
        "miata", "impreza", "rx7", "silvia", "evo",  
        "350z", "celica", "outback", "forester", "nsx",  
        "gt86", "brz", "crx", "accord", "legacy"
    ]

    # Escolhe uma palavra aleatoriamente
    palavra = random.choice(carros_japoneses)

    letras_descobertas = ['_' * len(palavra)]

    # Número de chances
    tentativas =  8

    # Lista de letras erradas
    letras_erradas = []

    while tentativas > 0:

        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", tentativas)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    letras_descobertas[i] = tentativa
        else:
            
            tentativas -= 1
            letras_erradas.append(tentativa)
# Programa principal:
