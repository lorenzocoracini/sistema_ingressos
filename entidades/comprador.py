from entidades.usuario import Usuario
from datetime import date


class Comprador(Usuario):
    def __init__(self, nome: str, cpf: int, nascimento: date, email: str, celular: int, saldo: float):
        super().__init__(nome, cpf, nascimento, email, celular, saldo)
        self.__historico_compras = []
        self.__eventos_favoritos = []

    @property
    def historico_compras(self):
        return self.__historico_compras

    @property
    def eventos_favoritos(self):
        return self.__eventos_favoritos
