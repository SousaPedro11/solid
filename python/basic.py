class Pessoa:
    def __init__(self, nome, cor, altura, sexo, carro=None):
        self.nome = nome
        self.cor = cor
        self.altura = altura
        self.sexo = sexo
        self.carro = carro

    def comprar_carro(self, carro):
        self.carro = carro

    def tem_carro(self):
        if self.carro:
            print(self.carro)
        else:
            print('Não tem carro')

    def __str__(self) -> str:
        return self.nome


class PessoaFisica(Pessoa):
    def __init__(self, nome, cor, altura, sexo, cpf):
        super().__init__(nome, cor, altura, sexo)
        self.cpf = cpf

    def __str__(self) -> str:
        return f'{self.nome}: {self.cpf}'


class PessoaJuridica(Pessoa):
    def __init__(self, nome, cor, altura, sexo, cnpj):
        super().__init__(nome, cor, altura, sexo)
        self.cnpj = cnpj

    def __str__(self) -> str:
        return f'{self.nome}: {self.cnpj}'


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def __str__(self) -> str:
        return self.modelo


pessoa = Pessoa('Pedro', 'branco', 1.71, 'M')
pessoaJuridica = PessoaJuridica(
    'Levy', 'branco', '0.5', 'indeciso', 'cnpjqualquer')
pessoaFisica = PessoaJuridica(
    'Aquim', 'branco', '1.75', 'indeciso', 'cpfqualquer')

carro = Carro('Fiesta')

print(pessoa)
print(pessoaFisica)
print(pessoaJuridica)
print(carro)
pessoaJuridica.comprar_carro(carro)

pessoa.tem_carro()
pessoaFisica.tem_carro()
pessoaJuridica.tem_carro()
