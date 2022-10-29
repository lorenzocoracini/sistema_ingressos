from entidades.comprador import Comprador


class Ingresso:
    def __init__(self, valor: float, codigo: int, lote: int):
        self.__valor = valor
        self.__codigo = codigo
        self.__lote = lote
        self.__comprador = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def lote(self):
        return self.__lote

    @lote.setter
    def lote(self, novo_lote):
        self.__lote = novo_lote

    @property
    def comprador(self):
        return self.__comprador

    @comprador.setter
    def comprador(self, novo_comprador):
        self.__comprador = novo_comprador

