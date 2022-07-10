from importlib import import_module
from eventos import Tamagotchi
from spritess import *
import os

#TITULO
#print_menuInicial = Sprites()
#print_menuInicial.titulo_do_jogo()

print('-'*50)
print('INICIAR JOGO')
print('-'*50)

personagem = int(input('Escolha seu personagem -->'))

if personagem >= 1 and personagem <= 3:
    nome = input('Digite o nome do seu pet: ')
    pet = Tamagotchi(nome, personagem)
else:
  exit("Esse personagem não existe, tente novamente")

os.system("cls")     
    
#MENU DE AÇÕES
op = None
pet.imprimirDados()
while op != 0:
        
    print('-'*50)
    print('SALA PRINCIPAL -- Interaja com seu pet!')
    print('-'*50)

    print('1-alimentar')
    print('2-brincar')
    print('3-Curar')
    print('4-Tomar banho')
    print('5-dormir')
    print('0-sair')
    op = int(input('Digite o número da ação desejada --> '))
        
    if op != 0:
        pet.virtual_pet.imprimeAcao(op)
        pet.event(op)  
    else:
        exit('Você saiu do jogo...')

