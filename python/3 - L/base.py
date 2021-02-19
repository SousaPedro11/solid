class Veiculo:
    def __init__(self, tipo) -> None:
        self.tipo = tipo


class Carro(Veiculo):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)


caminhao = Veiculo('caminhao')
caminhao.propriedades = {
    'cor': 'azul',
    'cambio': 'manual',
    'capacidade': '5'
}

carro = Carro('Sedan')
carro.propriedades = {'azul', 'automatico', 5}

kombi = Veiculo('kombi')
kombi.propriedades = ['azul', 'manual', 12]

veiculos = [caminhao, carro, kombi]


def buscar_por_cor(cor: str) -> None:
    for veiculo in veiculos:
        if veiculo.propriedades['cor'] == cor:
            print(veiculo)


buscar_por_cor('azul')
