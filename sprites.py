from math import e
import os

from pip import main

class Sprites:  #Esta classe irá "imprimir" as imagens dos personagens

    def __init__(self, choice):
       if choice > 3:
           exit('Erro ao selecionar o Tamagotchi, tente novamente!')
       else:
           self.__choice = choice

    @property
    def choice(self):
        return self.__choice

    def switchCharacter(self, op):
        if self.choice == 1:
            print('Você escolheu Febrix')
            if op == 1:
                os.system("cls") 
                print( "█████████\n█▄█████▄█\n█▼▼▼▼▼\n█  ██\n█▲▲▲▲▲\n█████████\n ██ ██\n")
            elif op == 2:
                os.system("cls")
                print("█████████  ╔═══╗♪\n█▄█████▄█  ║███║ ♫\n█▼▼▼▼▼     ║(●)║♫\n█████████  ╚═══╝ ♪\n ██ ██")
            elif op == 3:
                os.system("cls") 
                print('')
            elif op == 4:
                os.system("cls")
                print('')
            elif op == 5:
                os.system("cls") 
                print("█████████\n█▄█████▄█      ZzzZzzz\n█████████\n█████████\n ██ ██")
            else:
                pass
        elif self.choice == 2:
            print('Você escolheu Fantasminha')
            if op == 1:
                os.system("cls") 
                print('▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒ ▒ ▒ ▒')
            elif op == 2:
                os.system("cls") 
                print('▒▒▒▒▒▒▒╔═══╗♪\n▒─▄▒─▄▒║███║ ♫\n▒▒▒▒▒▒▒║ (●)  ║♫\n▒▒▒▒▒▒▒╚═══╝ ♪\n▒   ▒   ▒   ▒')
            elif op == 3:
                os.system("cls")
                print('')
            elif op == 4:
                os.system("cls")
                print('')
            elif op == 5:
                os.system("cls")
                print('▒▒▒▒▒▒▒\n▒─ ▒─ ▒   ZzzzZzzz\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒  ▒  ▒')
            else:
                pass
        elif self.choice == 3:
            print('Pacman')
            if op == 1:
                os.system("cls")
                print('▄████▄\n███▄█▀\n████     █     █\n█████▄\n ▀████▀')
            elif op == 2:
                os.system("cls")
                print('▄████▄  ╔═══╗♪\n███▄█▀  ║███║ ♫\n████        ║  (●)  ║♫\n█████▄  ╚═══╝ ♪\n ▀████▀')
            elif op == 3:
                os.system("cls")
                print('')
            elif op == 4:
                os.system("cls")
                print('')
            elif op == 5:
                os.system("cls")
                print('▄████▄\n███─█▀    ZzzzZzzz\n████\n█████▄\n ▀████▀\n')
            else:
                pass
        else:
            main()

            
       
    