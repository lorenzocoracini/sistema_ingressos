import sys

from controlador_comprador import ControladorComprador
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
        pass

    def inicia_produtor(self):
        pass

    def finaliza(self):
        sys.exit()

    def inicia(self):
        pass
