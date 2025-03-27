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

    #Lista de palavras para o jogo
    carros_japoneses = [
        "Civic", "Corolla", "Lancer", "Skyline", "Supra",  
        "Miata", "Impreza", "RX7", "Silvia", "Evo",  
        "350Z", "Celica", "Outback", "Forester", "NSX",  
        "GT86", "BRZ", "CRX", "Accord", "Legacy"
    ]

    #Escolhe uma palavra aleatoriamente
    palavra = random.choice(carros_japoneses)
    print('-' * len(palavra), end='\n')


# Programa principal:
print('- '* 8, end='\n')