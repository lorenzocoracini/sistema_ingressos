from usuario import Usuario


class Comprador(Usuario):
    def __init__(self, nome: str, cpf: str, nascimento: str, email: str, celular: int, saldo: float):
        super().__init__(nome, cpf, nascimento, email, celular)
        self.__saldo = saldo
        self.__historico_compras = []
        self.__eventos_favoritos = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def historico_compras(self):
        return self.__historico_compras

    @property
    def eventos_favoritos(self):
        return self.__eventos_favoritos
