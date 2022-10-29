from entidades.evento import Evento
from datetime import *
from telas.tela_evento import TelaEvento
from entidades.local import Local
from controladores.controlador_produtor import ControladorProdutor


class ControladorEvento:
    def __init__(self):
        self.__tela_evento = TelaEvento()


    def gerar_ingressos(self):
        pass