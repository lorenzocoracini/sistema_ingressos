import sys

from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ContraladorIngressos
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_evento = ControladorEvento()
        self.__controlador_ingressos = ContraladorIngressos()
        self.__controlador_comprador = ControladorComprador()
        self.__controlador_produtor = ControladorProdutor()

    def inicia_evento(self):
        pass

    def inicia_ingressos(self):
        pass

    def inicia_comprador(self):
        print('Inicia_comprador')

    def inicia_produtor(self):
        print('Inicia_produtor')

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.inicia_comprador, 2: self.inicia_produtor, 0: self.finaliza}

        while True:
            opcao = self.__tela_principal.mostra_tela_principal()
            metodo_escolihido = opcoes[opcao]
            metodo_escolihido()
