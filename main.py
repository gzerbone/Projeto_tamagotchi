from sprites import Sprites
from eventos import Tamagotchi
import os

#TITULO
print_titulo = Sprites()
print_titulo.titulo_do_jogo()

print('-'*50)
print('INICIAR JOGO')
print('-'*50)

menu = Sprites()
menu.menu_character()

personagem = int(input('Escolha um personagem? '))

aux = 0
while personagem >= 1 and personagem <= 3:
    
    if aux == 0:
        nome = input('Escolha o nome do seu tamagotchi: ')

        pet = Tamagotchi(nome, personagem)
        aux += 1
    else:
        exit()

    #MENU DE AÇÕES
    op = None
    while op != 0:
        
        print('-'*50)
        print('SALA PRINCIPAL -- Interaja com seu pet!')
        print('-'*50)

        print('1-alimentar')
        print('2-brincar')
        print('3-Curar')
        print('4-Limpar')
        print('5-dormir')
        print('0-sair')
        op = int(input('Digite o número da ação desejada --> '))
        
        if op != 0: #Composição
            pet.virtual_pet.switchCharacter(op)
            pet.event(op)  

        else:
            pass

exit("Esse personagem não existe, tente novamentellllllllllllll")