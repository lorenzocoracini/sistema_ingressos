from entidades.evento import Evento
from datetime import *
from telas.tela_evento import TelaEvento
from entidades.local import Local


class ControladorEvento:
    def __init__(self):
        self.__eventos = []
        self.__tela_evento = TelaEvento()

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pegar_dados()
        local = Local(dados_evento['rua_evento'], dados_evento['bairro_evento'],
                      dados_evento['cidade_evento'], dados_evento['cep_evento'],
                      dados_evento['lotacao_maxima'], dados_evento['aluguel'])

        evento = Evento(dados_evento['codigo_evento'], dados_evento['data_evento'], dados_evento['nome_evento'],
                        dados_evento['descricao_evento'], dados_evento['atracao_evento'], dados_evento['despesas_evento'],
                        local)

        if not self.retorna_evento_pelo_codigo(evento.codigo):
            self.__eventos.append(evento)

    def retorna_evento_pelo_codigo(self, codigo):
        for evento in self.__eventos:
            if evento.codigo == codigo:
                return evento

    @property
    def eventos(self):
        return self.__eventos

    def alterar_evento(self):
        pass

    def excluir_evento(self):
        pass

    def gerar_ingressos(self):
        pass