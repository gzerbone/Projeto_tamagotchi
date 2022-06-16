from ast import arg
from math import e
import os  #Usado para limpar a tela durante a utilização do programa

#Esta classe irá "imprimir" as imagens dos personagens
class Sprites:  
    def __init__(self, choice = 0): #inicializando com um numero qualquer para conseguir manipular o metodo de TITULO_DO_JOGO() na main
        self.__choice = choice

    #Get
    @property
    def choice(self):
        return self.__choice

    # FRASES
    @staticmethod
    def titulo_do_jogo():  # UESCGOTCHI
        print("\n")
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝")

    @staticmethod
    def menu_character():
        print("█████████       ▒▒▒▒▒▒▒       ▄████▄\n█▄█████▄█       ▒─▄▒─▄▒       ███▄█▀\n█▼▼▼▼▼          ▒▒▒▒▒▒▒       ████            \n█████████       ▒▒▒▒▒▒▒       █████▄\n ██ ██          ▒ ▒ ▒ ▒       ▀████▀\n FEBRIX         INIMIGO       PACMAN\n   (1)            (2)          (3)")

    def switchCharacter(self, option):
        if self.choice == 1:
            print('Você escolheu Febrix')
            if option == 1:
                os.system("cls") 
                print( "█████████\n█▄█████▄█\n█▼▼▼▼▼\n█  ██\n█▲▲▲▲▲\n█████████\n ██ ██\n")
            elif option == 2:
                os.system("cls")
                print("█████████  ╔═══╗♪\n█▄█████▄█  ║███║ ♫\n█▼▼▼▼▼     ║(●)║♫\n█████████  ╚═══╝ ♪\n ██ ██")
            elif option == 3:
                os.system("cls") 
                print('')
            elif option == 4:
                os.system("cls")
                print('')
            elif option == 5:
                os.system("cls") 
                print("█████████\n█▄█████▄█      ZzzZzzz\n█████████\n█████████\n ██ ██")
            else:
                pass
        elif self.choice == 2:
            print('Você escolheu Fantasminha')
            if option == 1:
                os.system("cls") 
                print('▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒ ▒ ▒ ▒')
            elif option == 2:
                os.system("cls") 
                print('▒▒▒▒▒▒▒╔═══╗♪\n▒─▄▒─▄▒║███║ ♫\n▒▒▒▒▒▒▒║ (●)  ║♫\n▒▒▒▒▒▒▒╚═══╝ ♪\n▒   ▒   ▒   ▒')
            elif option == 3:
                os.system("cls")
                print('')
            elif option == 4:
                os.system("cls")
                print('')
            elif option == 5:
                os.system("cls")
                print('▒▒▒▒▒▒▒\n▒─ ▒─ ▒   ZzzzZzzz\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒  ▒  ▒')
            else:
                pass
        elif self.choice == 3:
            print('Você escolheu Pacman')
            if option == 1:
                os.system("cls")
                print('▄████▄\n███▄█▀\n████     █     █\n█████▄\n ▀████▀')
            elif option == 2:
                os.system("cls")
                print('▄████▄  ╔═══╗♪\n███▄█▀  ║███║ ♫\n████        ║  (●)  ║♫\n█████▄  ╚═══╝ ♪\n ▀████▀')
            elif option == 3:
                os.system("cls")
                print('')
            elif option == 4:
                os.system("cls")
                print('')
            elif option == 5:
                os.system("cls")
                print('▄████▄\n███─█▀    ZzzzZzzz\n████\n█████▄\n ▀████▀\n')
            else:
                pass

            
            

            
       
    