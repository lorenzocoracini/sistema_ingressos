from telas.tela_evento import TelaEvento



class ControladorEvento:
    def __init__(self):
        self.__tela_evento = TelaEvento()


    def gerar_ingressos(self):
        lotacao_max = self.__tela_evento.pegar_dados()
        lotacao_max = lotacao_max['lotacao_maxima_evento']
        qtd_ingressos = 0
        while qtd_ingressos <= lotacao_max:
            ingresso()
