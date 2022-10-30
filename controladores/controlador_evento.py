from telas.tela_evento import TelaEvento
from entidades.evento import Evento


class ControladorEvento:
    def __init__(self):
        self.__tela_evento = TelaEvento()
        self.__eventos = []
        self.__evento = Evento


