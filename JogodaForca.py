# Jogo da forca em linguagem Python

#Imports:

import random
from os import system, name

#Classes:

# Classe cuidar das telas
class Recursos():
    def __init__(self):
        self.chances = 6
        self.estagios = [
            # Estágio 6 (final)
            '''
                -------
                |     |
                |     0
                |    \\|/
                |     |
                |    / \\
                |
                -
            ''',
            # Estágio 5
            '''
                -------
                |     |
                |     0
                |    \\|/
                |     |
                |    / 
                |
                -
            ''',
            # Estágio 4
            '''
                -------
                |     |
                |     0
                |    \\|/
                |     |
                |    
                |
                -
            ''',
            # Estágio 3
            '''
                -------
                |     |
                |     0
                |    \\|/
                |    
                |     
                |
                -
            ''',
            # Estágio 2
            '''
                -------
                |     |
                |     0
                |    \\|
                |    
                |    
                |
                -
            ''',
            # Estágio 1
            '''
                -------
                |     |
                |     0
                |   
                |    
                |    
                |
                -
            ''',
            # Estágio 0 (inicial)
            '''
                -------
                |     |
                |     
                |   
                |    
                |    
                |
                -
            '''
        ]

    # Método para limpar a tela a cada execução
    def limpaTela():
        # Windows
        if name == 'nt':
            _ = system('cls')
        
        # Mac ou Linux
        else:
            _ = system('clear')

    # Método para mostrar o boneco na tela
    def boneco(self):
        print(self.estagios[self.chances])    

    def inicia_jogo():
        print("\nBem vindo ao jogo da forca!!!")
        print("Dica: É um carro japônes")
        print("Adivinhe a palavra abaixo: \n")

class Escolha_da_Palavra():
    def __init__(self):
    # Instância que armazena todas as possiveis escolhas
        self.carros = [
            "civic", "corolla", "lancer", "skyline", "supra",  
            "miata", "impreza", "silvia", "evo", "celica",  
            "outback", "forester", "nsx", "brz", "crx",  
            "accord", "legacy"
        ]
        self.palavra = ""
        self.lista_letras_palavra = []

    def definir_palavra(self):
        # Escolhe uma palavra aleatoriamente
        self.palavra = random.choice(self.carros)
        self.lista_letras_palavra = [letra for letra in self.palavra]
        return self.palavra
    


# Classe que dá início ao jogo:
class Jogo():
    def __init__(self):
        tela = Recursos()
        palavra = Escolha_da_Palavra.definir_palavra()
        tela.limpaTela()

        tela.inicia_jogo()

        # Cria o tabuleiro
        letras_descobertas = ['_'] * len(palavra)

        # Número de chances
        tentativas =  6

        # Lista de letras erradas
        letras_erradas = []

        while tentativas > 0:

            # Print
            print(" ".join(letras_descobertas))
            print("\nChances restantes:", tentativas)
            print("Letras erradas:", " ".join(letras_erradas))
            print(boneco(tentativas))

            # Tentativa
            tentativa = input("Digite uma letra: ").lower()

            if tentativa in palavra:
                print("\nVocê acertou a letra!")

                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        letras_descobertas[i] = tentativa
            
            elif tentativa in letras_erradas or tentativa in letras_descobertas:
                print("\nEssa letra já foi tentada antes!")
                print("Tente outra letra.")
                
            else:
                tentativas -= 1
                letras_erradas.append(tentativa)

            # Checagem de vitória
            if "_" not in letras_descobertas:
                print("\n Você venceu!!!  ;)")
                print("A palavra era:", palavra)
                break
        
        # Checagem de derrota
        if "_" in letras_descobertas:
            print("\nVocê perdeu!!! :(")
            print("A palavra era:", palavra)
        
# Programa principal:
if __name__ == "__main__":
    jogo()
