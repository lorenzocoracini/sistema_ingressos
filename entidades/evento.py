from local import Local
from datetime import *


class Evento:
    def __init__(self, codigo: int, data:date, nome: str, horario: str, descricao: str, atracoes: [], ingressos: [],
                 depesas: float, local: Local):
        self.__codigo = codigo
        self.__data = data
        self.__nome = nome
        self.__horario = horario
        self.__descricao = descricao
        self.__atracoes = []
        self.__ingressos = ingressos
        self.__despesas = depesas
        self.__local = local


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
def horario(self):
    return self.__horario


@horario.setter
def horario(self, novo_horario):
    self.__horario = novo_horario


@property
def descricao(self):
    return self.__descricao


@descricao.setter
def descricao(self, nova_descricao):
    self.__descricao = nova_descricao


@property
def atracoes(self):
    return self.__atracoes


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
def local(self, novo_local):
    self.__local = novo_local
