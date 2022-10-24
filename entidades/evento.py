from entidades.local import Local
from datetime import datetime


# https://www.programiz.com/python-programming/datetime
class Evento:
    def __init__(self, codigo: int, data: datetime, nome: str, descricao: str, atracao: str, ingressos: [],
                 depesas: float):
        self.__codigo = codigo
        self.__data = data
        self.__nome = nome
        self.__descricao = descricao
        self.__atracao = atracao
        self.__ingressos = ingressos
        self.__despesas = depesas
        self.__local = None


@property
def codigo(self):
    return self.__codigo


@codigo.setter
def codigo(self, novo_codigo):
    self.__codigo = novo_codigo


@property
def data(self):
    return self.__data


@data.setter
def data(self, nova_data):
    self.__data = nova_data


@property
def nome(self):
    return self.__nome


@nome.setter
def nome(self, novo_nome):
    self.__nome = novo_nome


@property
def descricao(self):
    return self.__descricao


@descricao.setter
def descricao(self, nova_descricao):
    self.__descricao = nova_descricao


@property
def atracao(self):
    return self.__atracao


@atracao.setter
def atracao(self, nova_atracao):
    self.__atracao = nova_atracao


@property
def ingressos(self):
    return self.__ingressos


@property
def despesas(self):
    return self.__despesas


@despesas.setter
def despesas(self, novas_despesas):
    self.__despesas = novas_despesas


@property
def local(self):
    return self.__local


@local.setter
def local(self, rua, bairro, cidade, cep, lotacao_maxima, aluguel):
    self.__local = Local(rua, bairro, cidade, cep, lotacao_maxima, aluguel)
