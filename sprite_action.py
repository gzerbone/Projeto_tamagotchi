from re import X
from teste_sprite import Sprites

class Action:
    def __init__(self, choice):
        self.__choice = choice

    def comendo(self):
        x = Sprites.pacman_comendo()
        #fazer condição se ele ja está comendo ou se ele nao está comendo ainda