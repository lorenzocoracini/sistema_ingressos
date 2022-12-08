from entidades.local import Local
from datetime import datetime


class Evento:
    def __init__(self, codigo: int, data: str, nome: str, descricao: str, atracao: str,
                 local:Local):
        self.__codigo = codigo
        self.__data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        self.__nome = nome
        self.__descricao = descricao
        self.__atracao = atracao
        self.__local = local
        self.__ingressos = []
        self.__ingressos_vendidos = []


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

    @ingressos.setter
    def ingressos(self, ingressos):
        self.__ingressos = ingressos

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, rua, cep, lotacao_maxima):
        self.__local = Local(rua, cep, lotacao_maxima)

    @property
    def ingressos_vendidos(self):
        return self.__ingressos_vendidos

    @ingressos_vendidos.setter
    def ingressos_vendidos(self, ingressos):
        self.__ingressos_vendidos = ingressos