from abc import ABC, abstractmethod
from enum import Enum


class Time(Enum):
    AZUL = 1
    VERMELHO = 2
    PRETO = 3


class IntegrantesTimeVisualizador(ABC):

    @abstractmethod
    def buscar_todos_por_time(self, time):
        pass


class Jogador:
    def __init__(self, nome) -> None:
        self.nome = nome


class IntegranteTime(IntegrantesTimeVisualizador):
    def __init__(self) -> None:
        self.integrantes = []

    def adicionar_integrante(self, jogador, time):
        self.integrantes.append((jogador, time))

    def buscar_todos_por_time(self, time):
        for integrante in self.integrantes:
            if integrante[1] == time:
                yield integrante[0].nome


class Analise:
    def __init__(self, integrantes: IntegrantesTimeVisualizador) -> None:
        for integrante in integrantes.buscar_todos_por_time(Time.VERMELHO):
            print(f'{integrante} é do time vermelho')


jogador1 = Jogador('Chaves')
jogador2 = Jogador('Quico')
jogador3 = Jogador('Godinez')

integrantes_time = IntegranteTime()
integrantes_time.adicionar_integrante(jogador1, Time.AZUL)
integrantes_time.adicionar_integrante(jogador2, Time.VERMELHO)
integrantes_time.adicionar_integrante(jogador3, Time.PRETO)

Analise(integrantes_time)
