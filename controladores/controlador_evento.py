from entidades.evento import Evento
from time import *
from datetime import *


class ControladorEvento:
    def __init__(self):
        self.__eventos = []

    def adicionar_evento(self, codigo: int, data: date, nome:str, horario: time(), descricao: str, atracoes: [], ingressos: [],
                         despesas: float):

        evento = Evento(codigo, data, nome, horario, descricao, atracoes, ingressos, despesas)

        try:
            for e in self.__eventos:
                if evento.codigo == e.codigo:
                    raise Exception
            else:
                self.__eventos.append(evento)

        except Exception:
            return None

    def alterar_evento(self):
        pass

    def excluir_evento(self):
        pass
