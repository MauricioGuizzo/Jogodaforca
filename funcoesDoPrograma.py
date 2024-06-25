import os
from datetime import datetime

def limpar_tela ():
    os.system ("cls")
    
def menu_apresentacao():
    print('''
    
JOGO DA FORCA

| BY: Mauricio Guizzo |

''')

def ganhou():
    print('''
VOCE VENCEU
''')

def perdeu():
    print('''
VOCE PERDEU
''')