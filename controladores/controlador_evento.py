from telas.tela_evento import TelaEvento
from entidades.evento import Evento
from entidades.local import Local



class ControladorEvento:
    def __init__(self):
        self.__eventos = []
        self.__tela_evento = TelaEvento(self)

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pegar_dados()
        local = Local(dados_evento['rua_evento'], dados_evento['cep_evento'],
                      dados_evento['lotacao_maxima_evento'])

        evento = Evento(dados_evento['codigo_evento'], dados_evento['data_evento'], dados_evento['nome_evento'],
                        dados_evento['descricao_evento'], dados_evento['atracao_evento'],
                        local)
        if evento not in self.__eventos:
            self.__eventos.append(evento)

    def alterar_evento(self):
        codigo_evento, dados_atualizados = self.__tela_evento.alterar_evento()
        evento_a_ser_alterado = None
        for evento in self.__eventos:
            if evento.codigo == codigo_evento:
                evento_a_ser_alterado = evento
        if evento_a_ser_alterado:
            evento_a_ser_alterado.codigo = (dados_atualizados['codigo_evento'])
            evento_a_ser_alterado.data = (dados_atualizados['data_evento'])
            evento_a_ser_alterado.nome = (dados_atualizados['nome_evento'])
            evento_a_ser_alterado.descricao = (dados_atualizados['descricao_evento'])
            evento_a_ser_alterado.atracao = (dados_atualizados['atracao_evento'])

    def excluir_evento(self):
        codigo = self.__tela_evento.remover_evento()
        for evento in self.__eventos:
            if evento.codigo == codigo:
                self.__eventos.remove(evento)


    def listar_eventos(self):
        self.__tela_evento.mostar_eventos(self.__eventos)
