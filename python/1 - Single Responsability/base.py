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

    def salvar_para_arquivo(self, nome_arquivo: str, local: str) -> None:
        """Salva os registros em arquivo

        Args:
            nome_arquivo (str): Nome da agenda
            local (str): Path onde sera salvo
        """
        print(f'Agenda salva em \"{local}{nome_arquivo}\"')

    def salvar_em_banco(self, banco: str) -> None:
        """Salva os registros em banco de dados

        Args:
            banco (str): Referencia ao banco de dados
        """
        print(f'Agenda salva em \"{banco}\"')


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

agenda.salvar_para_arquivo('agenda.json', '~/Documentos/contatos/')
agenda.salvar_em_banco('agenda.db')
