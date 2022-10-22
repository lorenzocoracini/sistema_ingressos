from telas.tela_produtor import TelaProdutor


class ControladorProdutor:
    def __init__(self):
        self.__produtores = []
        self.__tela_produtor = TelaProdutor()

    def mostra_tela_opcoes(self):
        opcoes = {1: self.__tela_produtor.mostra_tela_login_produtor,
                  2: self.__tela_produtor.mostra_tela_cadastro_produtor}

        opcao = self.__tela_produtor.mostra_tela_produtor()
        metodo_escolihido = opcoes[opcao]
        metodo_escolihido()

    def inclui_produtor(self):
        pass

    def altera_produtor(self):
        pass

    def exclui_produtor(self):
        pass

    def listar_produtores(self):
        pass

    def adicionar_evento(self):
        pass

    def adicionar_venda_historico_vendas(self):
        pass

    def adicionar_evento_historico_eventos(self):
        pass

    def adicionar_evento_disponivel(self):
        pass

    def remover_evento_disponivel(self):
        pass

    def excluir_conta(self):
        pass