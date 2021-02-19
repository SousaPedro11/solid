from abc import ABC, abstractmethod


class DispositivoComunicacao(ABC):

    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    @abstractmethod
    def fazer_chamada(self, numero):
        pass

    @abstractmethod
    def enviar_sms(self, numero, mensagem):
        pass

    @abstractmethod
    def navegar_internet(self, url):
        pass

    def __str__(self) -> str:
        return self.modelo


class SmartPhone(DispositivoComunicacao):
    def fazer_chamada(self, numero):
        print(f'{self.modelo} discando para {numero}')

    def enviar_sms(self, numero, mensagem):
        print(f'{self.modelo} enviando \"{mensagem}\" para {numero}')

    def navegar_internet(self, url):
        print(f'{self.modelo} acessando {url}')


class TelefoneFixo(DispositivoComunicacao):
    def fazer_chamada(self, numero):
        print(f'{self.modelo} discando para {numero}')

    def enviar_sms(self, numero, mensagem):
        raise ValueError(f'{self.modelo} nao tem a funcao de enviar sms')

    def navegar_internet(self, url):
        raise ValueError(f'{self.modelo} nao tem a funcao de navegar')


celular = SmartPhone('redmi 7')
celular.fazer_chamada('9199999-9999')
celular.enviar_sms('9199877-8888', 'Eae meu chapa!')
celular.navegar_internet('https://www.github.com')

fixo = TelefoneFixo('Do ronca')
fixo.fazer_chamada('9199999-9999')
fixo.enviar_sms('9199877-8888', 'Eae meu chapa!')
fixo.navegar_internet('https://www.github.com')
