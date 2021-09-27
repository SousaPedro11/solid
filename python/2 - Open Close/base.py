from enum import Enum


class Produto(Enum):
    CAMISA = 1
    CAMISETA = 2
    CALCA = 3


class CalculadoraDeDesconto():
    def __init__(self, tipo_produto, preco: float) -> None:
        self.tipo_produto = tipo_produto
        self.preco = preco

    def obter_desconto(self):
        if self.tipo_produto == Produto.CAMISA:
            return self.preco - (self.preco * .1)
        elif self.tipo_produto == Produto.CAMISETA:
            return self.preco - (self.preco * .2)
        elif self.tipo_produto == Produto.CALCA:
            return self.preco - (self.preco * .3)


camisa = CalculadoraDeDesconto(Produto.CAMISA, 100)
camiseta = CalculadoraDeDesconto(Produto.CAMISETA, 100)
calca = CalculadoraDeDesconto(Produto.CALCA, 100)
print(camisa.obter_desconto())
print(camiseta.obter_desconto())
print(calca.obter_desconto())
