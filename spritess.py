from abc import ABC, abstractmethod
import os


class Sprites(ABC):

    @abstractmethod
    def sprite_alimentar(self):
        pass

    @abstractmethod
    def sprite_brincar(self):
        pass

    @abstractmethod
    def sprite_curar(self):
        pass

    @abstractmethod
    def sprite_banhar(self):
        pass

    @abstractmethod
    def sprite_dormir(self):
        pass


class Febrix(Sprites):
    def __init__(self) -> None:
        print("\n")
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝")

        print("█████████       ▒▒▒▒▒▒▒       ▄████▄\n█▄█████▄█       ▒─▄▒─▄▒       ███▄█▀\n█▼▼▼▼▼          ▒▒▒▒▒▒▒       ████            \n█████████       ▒▒▒▒▒▒▒       █████▄\n ██ ██          ▒ ▒ ▒ ▒       ▀████▀\n FEBRIX       FANTASMINHA     PACMAN\n   (1)            (2)          (3)")

    def sprite_alimentar(self):
        os.system("cls")
        print("█████████\n█▄█████▄█\n█▼▼▼▼▼\n█  ██\n█▲▲▲▲▲\n█████████\n ██ ██\n")

    def sprite_brincar(self):
        os.system("cls")
        print("█████████  ╔═══╗♪\n█▄█████▄█  ║███║ ♫\n█▼▼▼▼▼     ║(●)║♫\n█████████  ╚═══╝ ♪\n ██ ██")

    def sprite_curar(self):
        os.system("cls")
        print("█████████    ┌─┐\n█▄█████▄█  ┌─┘ └─┐\n█▼▼▼▼▼     └─┐ ┌─┘\n█████████    └─┘\n ██ ██ \n ")

    def sprite_banhar(self):
        os.system("cls")
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│ ┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘ └┘└┘└┘\n█████████\n█▄█████▄█\n█▼▼▼▼▼\n█████████\n ██ ██\n')

    def sprite_dormir(self):
        os.system("cls")
        print("█████████\n█─█████─█   ZzzZzzz\n█████████\n█████████\n ██ ██")

    def imprimeAcao(self, acao=0):
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()


class Fantasminha(Sprites):
    def __init__(self):
        print("\n")
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝")


    def sprite_alimentar(self):
        os.system("cls")
        print('▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▄▒▒▒  ▒\n▒ ▒ ▒ ▒')

    def sprite_brincar(self):
        os.system("cls")
        print(
            '▒▒▒▒▒▒▒╔═══╗♪\n▒─▄▒─▄▒║███║ ♫\n▒▒▒▒▒▒▒║ (●)  ║♫\n▒▒▒▒▒▒▒╚═══╝ ♪\n▒ ▒ ▒ ▒')

    def sprite_curar(self):
        os.system("cls")
        print('▒▒▒▒▒▒▒    ┌─┐\n▒─▄▒─▄▒  ┌─┘ └─┐\n▒▒▒▒▒▒▒  └─┐ ┌─┘\n▒▒▒▒▒▒▒    └─┘\n▒ ▒ ▒ ▒')

    def sprite_banhar(self):
        os.system("cls")
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│ ┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘ └┘└┘└┘\n▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒ ▒ ▒ ▒')

    def sprite_dormir(self):
        os.system("cls")
        print('▒▒▒▒▒▒▒\n▒─ ▒─ ▒   ZzzzZzzz\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒  ▒  ▒')

    def imprimeAcao(self, acao=0):
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()


class Pacman(Sprites):

    def sprite_alimentar(self):
        os.system("cls")
        print('▄████▄\n███▄█▀\n████     █     █\n█████▄\n ▀████▀')

    def sprite_brincar(self):
        os.system("cls")
        print('▄████▄  ╔═══╗♪\n███▄█▀  ║███║ ♫\n████        ║  (●)  ║♫\n█████▄  ╚═══╝ ♪\n ▀████▀')

    def sprite_curar(self):
        os.system("cls")
        print('▄████▄    ┌─┐\n███▄█▀  ┌─┘ └─┐\n████    └─┐ ┌─┘\n█████▄    └─┘\n ▀████▀')

    def sprite_banhar(self):
        os.system("cls")
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘└┘└┘└┘\n▄████▄\n███▄█▀\n████    \n█████▄\n ▀████▀')

    def sprite_dormir(self):
        os.system("cls")
        print('▄████▄\n███─█▀    ZzzzZzzz\n████\n█████▄\n ▀████▀\n')

    def imprimeAcao(self, acao=0):
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()
