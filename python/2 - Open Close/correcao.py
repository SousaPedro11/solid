from abc import ABC, abstractmethod


class CalculadoraDeDesconto(ABC):

    def __init__(self, preco) -> None:
        self.preco = preco

    @abstractmethod
    def obter_desconto(self):
        pass


class CalculadoraDeDescontoCamisa(CalculadoraDeDesconto):

    def obter_desconto(self):
        return self.preco - (self.preco * .1)


class CalculadoraDeDescontoCamiseta(CalculadoraDeDesconto):

    def obter_desconto(self):
        return self.preco - (self.preco * .2)


class CalculadoraDeDescontoCalca(CalculadoraDeDesconto):

    def obter_desconto(self):
        return self.preco - (self.preco * .3)


camisa = CalculadoraDeDescontoCamisa(100)
camiseta = CalculadoraDeDescontoCamiseta(100)
calca = CalculadoraDeDescontoCalca(100)
print(camisa.obter_desconto())
print(camiseta.obter_desconto())
print(calca.obter_desconto())
