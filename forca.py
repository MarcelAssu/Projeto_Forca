# MARCEL ASSUNÇÃO DA SILVA, RA: 1136750 e # LEONARDO PASA CAMBRUSSI, RA: 1136187 

# PARA MELHOR EXPERIÊNCIA, ANTES DE RODAR A APLICAÇÃO, RODE O SEGUINTE CÓDIGO NA TELA DE TERMINAL VS CODE:
# python -m pip install rich
# APÓS, BASTA FECHAR O VS CODE E ABRÍ-LO NOVAMENTE E O CÓDIGO RODARÁ NORMALMENTE!

import os
import time
from rich import print


def limpar_Tela():
    os.system("cls")


quer_jogar = True

while quer_jogar == True:
    
    limpar_Tela()

    print("""[cyan1]
     ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄       ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░▌     ▐░░▌     ▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌      ▐░▌           ▐░▌  ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌       ▐░▌▐░▌          ▐░▌▐░▌ ▐░▌▐░▌       ▐░▌         ▐░▌       ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌        ▐░▌       ▐░▌        ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌         ▐░▌     ▐░▌         ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌          ▐░▌   ▐░▌          ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌           ▐░▌ ▐░▌           ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌            ▐░▐░▌        ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░▌        ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀               ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀ 
    [/]""")

    time.sleep(1.5)
    limpar_Tela()

    print("""[turquoise2]
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
    ▐░░░░░░░░░░░▌▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░▌       ▐░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌      ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
    [/]""")

    time.sleep(1.5)
    limpar_Tela()

    print("""[dodger_blue2]
     ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄  ▄  ▄ 
    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌▐░▌▐░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌▐░▌▐░▌
    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌▐░▌▐░▌
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌
    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌▐░▌▐░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌          ▐░▌       ▐░▌ ▀  ▀  ▀ 
    ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌ ▄  ▄  ▄ 
    ▐░░░░░░░░░░▌ ▐░▌       ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░▌▐░▌
     ▀▀▀▀▀▀▀▀▀▀   ▀         ▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀  ▀  ▀ 
    [/]""")

    time.sleep(1.5)
    limpar_Tela()

    print("""[dark_turquoise]
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌             ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌             ▐░▌          ▐░▌          
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
    ▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  ▐░▌                    ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌                       ▐░▌▐░▌          
    ▐░▌       ▐░▌▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌              ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀         ▀  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀               ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
    [/]""")

    time.sleep(1.5)
    limpar_Tela()

    print("""[dark_turquoise]
     ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ 
    ▐░▌       ▐░▌               ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌     ▐░▌  
    ▐░▌       ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌      ▐░▌ 
    ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
     ▀         ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
    [/]""")                                                          

    time.sleep(2)
    limpar_Tela()

    erros = 0
    tentativas = 6
    letras_usadas = []
    
    confere_desafiante = True
    confere_competidor = True
    confere_palavra_chave = True
    confere_dica1 = True
    confere_dica2 = True
    confere_dica3 = True
    
    while confere_desafiante == True:
        
        limpar_Tela()
        desafiante_nome = input("Desafiante, qual é o seu nome? ")
        limpar_Tela()
        
        if len(desafiante_nome) <= 1:
            print("Digite um nome válido!")
            time.sleep(3)
            confere_desafiante = True
        else:
            confere_desafiante = False
            
    while confere_competidor == True:
        
        limpar_Tela()   
        competidor_nome = input("Competidor, qual é o seu nome? ") 
        limpar_Tela()
        
        if len(competidor_nome) <= 1:
            print("Digite um nome válido!")
            time.sleep(3)
            confere_competidor = True
        else:
            confere_competidor = False
            
            
    while confere_palavra_chave == True:
        
        limpar_Tela()
        palavra_chave = input(F"{desafiante_nome}, digite a palavra para este o jogo: ").lower()
        limpar_Tela()
        
        if len(palavra_chave) <= 1:
            print("Digite uma palavra válida!")
            time.sleep(3)
            confere_palavra_chave = True
        else:
            confere_palavra_chave = False
        
    dicas = []
            
    while confere_dica1 == True:
        
        limpar_Tela()
        dica1 = input(F"{desafiante_nome}, digite a dica de n° 1: ")
        limpar_Tela()
        
        if len(dica1) <= 1:
            print("Digite uma dica válida!")
            time.sleep(3)
            confere_dica1 = True
        else:
            confere_dica1 = False
    
    while confere_dica2 == True:
        
        limpar_Tela()
        dica2 = input(F"{desafiante_nome}, digite a dica de n° 2: ")
        limpar_Tela()
        
        if len(dica2) <= 1:
            print("Digite uma dica válida!")
            time.sleep(3)
            confere_dica2 = True
        else:
            confere_dica2 = False
        
    while confere_dica3 == True:
        
        limpar_Tela()
        dica3 = input(F"{desafiante_nome}, digite a dica de n° 3: ")
        limpar_Tela()
        
        if len(dica3) <= 1:
            print("Digite uma dica válida!")
            time.sleep(3)
            confere_dica3 = True
        else:
            confere_dica3 = False
        
    dicas.append(dica1)
    dicas.append(dica2)
    dicas.append(dica3)
    
    status = ["*"] * len(palavra_chave)
    dicas_usadas = 0

    dicas_mostrar = []
    
    def uma_letra():
        if len(letra) > 1:
            print("[gold1]SÓ PODE DIGITAR 1 LETRA POR VEZ!!")
            time.sleep(3)
            limpar_Tela()
            
            
    def letra_repetida():
        print("[gold1]Você já utilizou esta letra!")
        time.sleep(3)
        limpar_Tela()
        
        letra = input("Qual letra você quer chutar agora?")
    
    while erros < tentativas and ''.join(status) != palavra_chave :
        
        limpar_Tela()
        tentativas_restantes = tentativas - erros
        
        print("A palavra escolhida tem este total de letras:\n")
        for i in status:
            print(i, end=" ")
            
        print("\n\n")
        print("Digite (1) para chutar uma letra.")
        print("Digite (2) para solicitar uma dica.")
        print("Digite (3) para ver seu status na partida.")
        print("Digite (4) para ver as dicas já usadas.")
        print("Digite (5) se você sabe a palavra inteira!")
        
        opcao = input("")

        if opcao == "1":
            
            limpar_Tela()
            
            letra = input("Qual letra você quer chutar agora?").lower()
            
            uma_letra()
                
            while letra in letras_usadas:
                letra_repetida()
            
                
            letras_usadas.append(letra)
            
            
            if letra in palavra_chave:
                print("Isto aí!! Esta letra está [spring_green1]CORRETA!")
                for i in range(len(palavra_chave)):
                    
                    if letra == palavra_chave[i] and len(letra) == 1:
                        status[i] = letra
                        time.sleep(3)
            else:
                print("Que pena, esta letra está [red1]INCORRETA!")
                erros = erros + 1
                time.sleep(3)
                
            
        
        elif opcao == "2":
            limpar_Tela()
            
            if dicas_usadas == 0:
                print("Dica nº 1:", dicas[0])
                dicas_usadas = dicas_usadas + 1
                dicas_mostrar.append(dicas[0])
                letra = input("Qual letra você quer chutar agora?").lower()
                uma_letra()
                
                while letra in letras_usadas:
                    letra_repetida()
                    
                letras_usadas.append(letra)
                
                
                if letra in palavra_chave:
                    print("Isto aí!! Esta letra está [spring_green1]CORRETA!")
                    for i in range(len(palavra_chave)):
                        
                        if letra == palavra_chave[i]:
                            status[i] = letra
                            time.sleep(3)
                else:
                    print("Que pena, esta letra está [red1]INCORRETA!")
                    erros = erros + 1
                    time.sleep(3)
                
                
            elif dicas_usadas == 1:
                print("Dica nº 2:", dicas[1])
                dicas_usadas = dicas_usadas + 1
                dicas_mostrar.append(dicas[1])
                letra = input("Qual letra você quer chutar agora?").lower()
                uma_letra()
                
                while letra in letras_usadas:
                    letra_repetida()
                    
                letras_usadas.append(letra)
                
                
                if letra in palavra_chave:
                    print("Isto aí!! Esta letra está [spring_green1]CORRETA!")
                    for i in range(len(palavra_chave)):
                        
                        if letra == palavra_chave[i]:
                            status[i] = letra
                            time.sleep(3)
                else:
                    print("Que pena, esta letra está [red1]INCORRETA!")
                    erros = erros + 1
                    time.sleep(3)
                
                
            elif dicas_usadas == 2:
                print("Dica nº 3:", dicas[2])
                dicas_usadas = dicas_usadas + 1
                dicas_mostrar.append(dicas[2])
                letra = input("Qual letra você quer chutar agora?").lower()
                uma_letra()
                
                while letra in letras_usadas:
                    letra_repetida()
                    
                letras_usadas.append(letra)
                
                
                if letra in palavra_chave:
                    print("Isto aí!! Esta letra está [spring_green1]CORRETA!")
                    for i in range(len(palavra_chave)):
                        
                        if letra == palavra_chave[i]:
                            status[i] = letra
                            time.sleep(3)
                else:
                    print("Que pena, esta letra está [red1]INCORRETA!")
                    erros = erros + 1
                    time.sleep(3)
                
            else:
                print("[gold1]Você já utilizou todas as dicas disponíveis!")
                time.sleep(3)
                
        elif opcao == "3":
            
            limpar_Tela()
            print("Você atualmente tem", erros, "erros na partida!")
            print("Você ainda possui", tentativas_restantes, "tentativas")
            time.sleep(3)
            
            
        elif opcao == "4":
            
            limpar_Tela()
            if dicas_usadas == 0:
                print("Você ainda não usou nenhuma dica!")
                time.sleep(3)
                
            else:
                print("Essas são as dicas já mostradas:\n")
                for dica in dicas_mostrar:
                    print("Dica: ",dica)
                    time.sleep(4)
            
        
        elif opcao == "5":
            limpar_Tela()
            
            palavra_inteira = input("Digite a palavra inteira: ").lower()
            if palavra_inteira == palavra_chave:
                status = palavra_chave
            else:
                print("Arriscou e [red1]ERROU!!")
                erros = erros + 1
                time.sleep(3) 
        
        else:
            print("[red1]Opção Inválida! Digite um dos números indicados")
            time.sleep(2)

    limpar_Tela()
    if erros == tentativas:
        print("Suas tentativas acabaram!")
        print(f"{palavra_chave} era a palavra!")
        time.sleep(4)
        limpar_Tela()
        
        print(f"{competidor_nome} [red1]PERDEU!") 
        print(f"{desafiante_nome} [spring_green1]GANHOU O JOGO!!")
        time.sleep(4)
        
    else:
        print("A palavra foi descoberta!!\n")
        print(f"{palavra_chave} era a palavra!")
        time.sleep(4)
        limpar_Tela()
        
        print(f"{desafiante_nome} [red1]PERDEU!") 
        print(f"{competidor_nome} [spring_green1]GANHOU O JOGO!!")
        time.sleep(4)
        
    limpar_Tela()
    
    menu = True
    while menu == True:
        limpar_Tela()
        print("Você gostaria de jogar mais uma partida?")
        
        print("Digite (1) para jogar mais uma vez")
        print("Digite (2) para encerrar o jogo")
        
        opcao_final = input()
        
        if opcao_final == "1":
            menu = False
            quer_jogar = True
            
        elif opcao_final == "2":
            menu = False
            quer_jogar = False
        
        else:
            print("[red1]Opção Inválida! Digite um dos números indicados")
            time.sleep(2)



print("""[sea_green2] 
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄      
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     
▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀ 
[/]""")
time.sleep(1.5)
limpar_Tela()

print("""[chartreuse3]
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄    
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌   
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌   
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌     ▐░▌          ▐░▌       ▐░▌           ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌   
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌           ▐░▌    ▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌   
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌           ▐░▌    ▐░▌       ▐░▌▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌   
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀           ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀            ▐░▌    ▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌   
▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌            ▐░▌     ▐░▌          ▐░▌     ▐░▌             ▐░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌   
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌       ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌
 ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀ 
[/]""")
time.sleep(1.5)
limpar_Tela()

print("""[dark_cyan]
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄  ▄  ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌▐░▌▐░▌
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌▐░▌▐░▌
▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌▐░▌▐░▌
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌▐░▌▐░▌
▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌▐░▌▐░▌
▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌▐░▌▐░▌
▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌               ▐░▌      ▀  ▀  ▀ 
▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌       ▐░▌▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌      ▄  ▄  ▄ 
▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌▐░▌▐░▌
 ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀  ▀  ▀      
[/]""")
time.sleep(3)
limpar_Tela() 