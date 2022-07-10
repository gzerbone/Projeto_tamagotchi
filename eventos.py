import os
from xmlrpc.client import boolean

from numpy import bool_
from spritess import *

class Tamagotchi:
    def __init__(self, nome:str = 'Buzz', opcao:int = None) -> None:
        if opcao == 1:
            self.virtual_pet = Febrix()
        elif opcao == 2:
            self.virtual_pet = Fantasminha()
        elif opcao == 3:
            self.virtual_pet = Pacman()

        self.__nome = nome
        self.__alimentacao = 30
        self.__felicidade = 100
        self.__saude = 100
        self.__higiene = 100
        self.__energia = 100
        self.__level = 0
        self.__xp = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def level(self):
        return self.__level

    @property
    def alimentacao(self):
        return self.__alimentacao

    @property
    def felicidade(self):
        return self.__felicidade

    @property
    def saude(self):
        return self.__saude

    @property
    def higiene(self):
        return self.__higiene

    @property
    def energia(self):
        return self.__energia

    @property
    def xp(self):
        return self.__xp  

    def subirXP(self):
        limite = 100
        level_max = 10
        if self.level < level_max:
            self.__xp += 25
            if self.__xp >= limite:
                self.__level += 1
                self.__xp = 0
                limite += 50

    def verificaEstadoAtual(self) -> bool: #verificar se ele morreu já antees da iteração, pois tava dando erro(explicar a zerbs, n esquece)
        if (self.__alimentacao <= 0) or (self.__felicidade <= 0) or (self.__saude <= 0) or (self.__higiene <= 0) or (self.__energia <= 0):
            return False #caso algum dos atributos tenha zerado, retorna false 
        else:
            return True

    def alteraAtributos(self, atributo:str) -> None:
        if atributo == 'alimentacao':
            if self.verificaEstadoAtual() == False:
                self.morrer()
            elif self.__alimentacao > 100:
                self.__alimentacao = 100
            else:
                self.__alimentacao += 10
                self.__energia -= 10
                self.__higiene -= 5
        
        elif atributo == 'felicidade':
            if self.verificaEstadoAtual() == False:
                self.morrer()
            elif self.__felicidade > 100:
                self.__felicidade = 100
            else:
                self.__felicidade += 15
                self.__alimentacao -= 15
                self.__energia -= 20
                self.__higiene -= 20

        elif atributo == 'saude':
            if self.verificaEstadoAtual() == False:
                self.morrer()
            elif self.__saude > 100:
                self.__saude = 100
            else:
                self.__saude += 30
                self.__alimentacao -= 20
                self.__energia += 30

        elif atributo == 'higiene':
            if self.verificaEstadoAtual() == False:
                self.morrer()
            elif self.__higiene >= 100:
                self.__higiene = 100
            else:
                self.__higiene = 100
                self.__alimentacao -= 5
                self.__energia -= 10

        elif atributo == 'energia':
            if self.verificaEstadoAtual() == False:
                self.morrer()
            elif self.__energia >= 100:
                self.__energia = 100
            else:
                self.__energia = 100
                self.__felicidade -= 30
                self.__alimentacao -= 30

    def alimentar(self) -> None:
        if self.alimentacao == 100:
            print(f'{self.nome} não está com fome')
        else:
            print(f'{self.nome} está se alimentando...')
            self.alteraAtributos('alimentacao')
            self.subirXP()
    
    def brincar(self) -> None:
        if self.felicidade == 100:
            print(f'{self.nome} ja brincou demais por hoje, tente mais tarde!')
        else:
            print(f'{self.nome} está se divertindo muito nesse momento!')
            self.alteraAtributos('felicidade')
            self.subirXP()

    def curar(self) -> None:
        if self.saude > 60:
            print(f'{self.nome} não precisa de medicamentos, ele está saudável')
        else:
            print(f'É sempre bom cuidar de quem você ama, {self.nome} está sendo medicado')
            self.alteraAtributos('saude')
            self.subirXP()

    def limpar(self) -> None:
        if self.higiene >= 60:
            print(f'{self.nome} já está limpo, poupe a água do planeta! :)')
        else:
            print('Hora do Banho!')
            self.alteraAtributos('higiene')
            self.subirXP()
    
    def dormir(self) -> None:
        if self.energia >= 60:
            print(f'{self.nome} não está com sono, aproveite-o e entretenha-o!')
        else:
            print(f'Shhhhh... {self.nome} está dormindo, faça silêncio')
            self.alteraAtributos('energia')
            self.subirXP()

    def morrer(self) -> None:
        exit('Game-Over, Jogador!')

    def imprimirDados(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'LEVEL: {self.level} e XP: {self.xp}')
        print(f'ALIMENTAÇÃO: {self.alimentacao}%')
        print(f'DIVERSÃO: {self.felicidade}%')
        print(f'SAÚDE: {self.saude}%')
        print(f'HIGIENE: {self.higiene}%')
        print(f'ENERGIA: {self.energia}%')
        print('\n')

    def event(self, opcao = 0) -> None:
        if opcao == 1:
            self.alimentar()
            self.imprimirDados()
        elif opcao == 2:
            self.brincar()
            self.imprimirDados()
        elif opcao == 3:
            self.curar()
            self.imprimirDados()
        elif opcao == 4:
            self.limpar()
            self.imprimirDados()
        elif opcao == 5:
            self.dormir()
            self.imprimirDados()
        elif opcao == 0:
            exit('Programa Finalizado com sucesso!')
           

