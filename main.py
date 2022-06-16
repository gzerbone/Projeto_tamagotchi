from sprites import Sprites
from eventos import Tamagotchi
#from testezin import Dino
import os

print('-'*50)
print('INICIAR JOGO')
print('-'*50)

nome = input('Escolha o nome do seu tamagotchi: ')
personagem = int(input('Qual o personagem escolhido? '))

pet = Tamagotchi(nome, personagem)
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
    
    if op != 0:    
        pet.virtual_pet.switchCharacter(op)
        pet.event(op)   
    else:
        pass
