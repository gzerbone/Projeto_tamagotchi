from sprite import Sprites
from eventos import Tamagotchi

personagem = Sprites(1)
virtual_pet = Tamagotchi('Febrix')

virtual_pet.alimentar()


escolhaDoPersonagem = input("->")

#Utilizando Associação
if escolhaDoPersonagem == 1:
    pass


if escolhaDoPersonagem == 2:
    pass


if escolhaDoPersonagem == 3:
    pass
#condições de escolha do personagem:
#se personagem == 1 entao o programa inteiro será baseado em febrix
#se personagem == 2 entao o programa inteiro será baseado em inimigo_pacman
#se personagem == 3 entao o programa inteiro será baseado em pacman()

