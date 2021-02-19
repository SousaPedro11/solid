class Veiculo:
    def __init__(self, tipo) -> None:
        self.tipo = tipo
        self.propriedades = {}

    def get_propriedades(self):
        return self.propriedades

    def set_propriedades(self, cor: str, cambio: str, capacidade: int) -> None:
        self.propriedades = {
            'cor': cor,
            'cambio': cambio,
            'capacidade': capacidade
        }

    def __str__(self) -> str:
        prop_str = ", ".join([str(valor) for valor in self.get_propriedades()
                              .values()])
        return f'{self.tipo}: {prop_str}'


class Carro(Veiculo):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)


caminhao = Veiculo('caminhao')
caminhao.set_propriedades('azul', 'manual', 6)


carro = Carro('Sedan')
carro.set_propriedades('azul', 'automatico', 5)

kombi = Veiculo('kombi')
kombi.set_propriedades('azul', 'manual', 12)

veiculos = [caminhao, carro, kombi]


def buscar_por_cor(cor: str) -> None:
    for veiculo in veiculos:
        if veiculo.get_propriedades()['cor'] == cor:
            print(veiculo)


buscar_por_cor('azul')
