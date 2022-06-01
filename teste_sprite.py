import string
from sprite_action import Action

class Sprites:  #Esta classe irá "criar" as imagens dos personagens

    def __init__(self, choice):
        self.__choice = choice


    #FRASES
    @staticmethod
    def nome():  #UESCGOTCHI
        print("\n")
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝")

    @staticmethod
    def escolha_frase(): #choose the caracter
        print("       _                            _   _                                     _              \n      | |                          | | | |                                   | |           _ \n   ___| |__   ___   ___  ___  ___  | |_| |__   ___    ___ __ _ _ __ __ _  ___| |_ ___ _ __(_)\n  / __| '_ \ / _ \ / _ \/ __|/ _ \ | __| '_ \ / _ \  / __/ _` | '__/ _` |/ __| __/ _ | '__|  \n | (__| | | | (_) | (_) \__ |  __/ | |_| | | |  __/ | (_| (_| | | | (_| | (__| ||  __| |   _ \n  \___|_| |_|\___/ \___/|___/\___|  \__|_| |_|\___|  \___\__,_|_|  \__,_|\___|\__\___|_|  (_)\n")

    @staticmethod
    #PERSONAGENS
    def escolha_personagem():  # O personagem parado
        print("█████████       ▒▒▒▒▒▒▒       ▄████▄\n█▄█████▄█       ▒─▄▒─▄▒       ███▄█▀\n█▼▼▼▼▼          ▒▒▒▒▒▒▒       ████            \n█████████       ▒▒▒▒▒▒▒       █████▄\n ██ ██          ▒ ▒ ▒ ▒       ▀████▀\n FEBRIX         INIMIGO       PACMAN\n   (1)            (2)          (3)")
        print("\n")
        print("—"*50)

    #FEBRIX
    def febrix(self):  # O personagem parado
        self.__choice = Action('parado')

        print("█████████       █████████\n█▄█████▄█       █▄█████▄█\n█▼▼▼▼▼          █▼▼▼▼▼\n█████████       █████████\n ██ ██           ██ ██\n")


    def febrix_ouvindo_musica(self):
        print("█████████  ╔═══╗♪\n█▄█████▄█  ║███║ ♫\n█▼▼▼▼▼     ║(●)║♫\n█████████  ╚═══╝ ♪\n ██ ██")


    #INIMIGO DO PACMAN
    def inimigo_pacman(self):
        print("▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒ ▒ ▒ ▒")


    def inimigo_comendo(self):
        print("▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒   █\n▒▒▒▄▒▒▒\n▒ ▒ ▒ ▒")

    #PACMAN
    def pacman(self):
        print("▄████▄\n███▄█▀\n████            \n█████▄\n ▀████▀")

    def pacman_comendo(self):
        print("▄████▄\n███▄█▀\n████     █     █\n█████▄\n ▀████▀")
