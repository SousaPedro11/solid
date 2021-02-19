from abc import ABC, abstractclassmethod


class Agenda:
    def __init__(self) -> None:
        """Metodo construtor
        """
        self.agenda = {}

    def adicionar_registro(self, nome: str, numero: str) -> None:
        """Adiciona uma entrada na agenda

        Args:
            nome (str): Nome do contato
            numero (str): Telefone do contato
        """
        self.agenda[nome] = numero

    def excluir_registro(self, nome: str) -> None:
        """Exclui um contato da agenda

        Args:
            nome (str): Nome do contato
        """
        self.agenda.pop(nome)

    def atualizar_registro(self, nome: str, numero: str) -> None:
        """Atualiza o numero de um contato

        Args:
            nome (str): Nome do contato
            numero (str): Telefone do contato
        """
        self.agenda[nome] = numero

    def obter_numero(self, nome: str) -> str:
        """Busca o numero de determinado contato

        Args:
            nome (str): Nome do contato

        Returns:
            str: Telefone do respectivo contato
        """
        return f"Telefone de {nome}: {self.agenda[nome]}"

    def __str__(self) -> str:
        """Sobrescrita do builtin equivalente ao toString em outras linguagens

        Returns:
            str: Retorna os registros da agenda em linhas
        """
        registros = [f'{nome}: {numero}' for nome,
                     numero in self.agenda.items() if len(self.agenda) > 0]
        return '\n'.join(registros)


class Salvar(ABC):
    @abstractclassmethod
    def salvar(self, objeto, local):
        print(f'Agenda salva em \"{local}\"')


class SalvarArquivo(Salvar):
    def salvar(self, objeto, local):
        """Salva os registros em arquivo

        Args:
            objeto (str): Agenda
            local (str): Path onde sera salvo
        """
        # TODO logica doida
        return super().salvar(objeto, local)


class SalvarBanco(Salvar):
    def salvar(self, objeto, local):
        """Salva os registros em banco de dados

        Args:
            objeto (str): Agenda
            local (str): Referencia ao banco de dados
        """
        # TODO logica doida
        return super().salvar(objeto, local)


agenda = Agenda()
agenda.adicionar_registro("Pedro", "+5591977776666")
agenda.adicionar_registro("Wendel", "+5591988888888")
agenda.atualizar_registro("Wendel", "+5591924242424")

print(agenda, "\n")

agenda.excluir_registro("Wendel")
agenda.adicionar_registro("Wewe", "+5591924242424")
agenda.atualizar_registro("Pedro", "+5591999680000")

print(agenda.obter_numero("Pedro"), "\n")

print(agenda, "\n")

SalvarArquivo().salvar(agenda, '~/Documentos/contatos/agenda.json')
SalvarBanco().salvar(agenda, 'agenda.db')
