from entidades.usuario import Usuario
from datetime import date

class Produtor(Usuario):
    def __init__(self, nome: str, cpf: str, nascimento: date, email: str, celular: int, senha: str):
        super().__init__(nome, cpf, nascimento, email, celular, senha)
        self.__historico_vendas = []
        self.__historico_eventos = []
        self.__eventos_disponiveis = []

    @property
    def historico_vendas(self):
        return self.__historico_vendas

    @property
    def historico_eventos(self):
        return self.__historico_eventos

    @property
    def eventos_disponiveis(self):
        return self.__eventos_disponiveis