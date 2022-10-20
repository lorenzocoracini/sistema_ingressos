import sys

from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ContraladorIngressos
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal
from telas.tela_produtor import TelaProdutor
from telas.tela_comprador import TelaComprador


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__tela_produtor = TelaProdutor()
        self.__tela_comprador = TelaComprador()
        self.__controlador_evento = ControladorEvento()
        self.__controlador_ingressos = ContraladorIngressos()
        self.__controlador_comprador = ControladorComprador()
        self.__controlador_produtor = ControladorProdutor()

    def inicia_evento(self):
        pass

    def inicia_ingressos(self):
        pass

    def inicia_comprador(self):
        opcoes = {1: self.__tela_comprador.mostra_tela_login_comprador,
                  2: self.__tela_comprador.mostra_tela_cadastro_comprador}

        while True:
            opcao = self.__tela_comprador.mostra_tela_comprador()
            metodo_escolihido = opcoes[opcao]
            metodo_escolihido()

    def inicia_produtor(self):
        opcoes = {1: self.__tela_produtor.mostra_tela_login_produtor,
                  2: self.__tela_produtor.mostra_tela_cadastro_produtor}

        while True:
            opcao = self.__tela_produtor.mostra_tela_produtor()
            metodo_escolihido = opcoes[opcao]
            metodo_escolihido()

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.inicia_comprador, 2: self.inicia_produtor, 0: self.finaliza}

        while True:
            opcao = self.__tela_principal.mostra_tela_principal()
            metodo_escolihido = opcoes[opcao]
            metodo_escolihido()
