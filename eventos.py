from sprite import Sprites

class Tamagotchi:
    def __init__(self, personagem:str):
        self.escolha = Sprites(personagem)
        self.__personagem = personagem
        self.__alimentacao = 3
        self.__auxiliar = None
        self.__diversao = 10
        self.__saude = 10
        self.__exaustao = 0

    @property
    def personagem(self):
        return self.__personagem

    @property
    def alimentacao(self):
        return self.__alimentacao


    #GETTER auxiliar
    @property
    def auxiliar(self):
        return self.__auxiliar

    @auxiliar.setter
    def auxiliar(self, auxiliar):
        self.__auxiliar = auxiliar


    def alimentar(self):
        if self.alimentacao == 10:
            print(f'{self.personagem} não está com fome')
            
            print(self.escolha.febrix())
        else:
            print(self.escolha.febrix_comendo())

            print(f'{self.personagem} está se alimentando...')
            self.__alimentacao += 1
            self.__exaustao += 1
            self.__saude += 1