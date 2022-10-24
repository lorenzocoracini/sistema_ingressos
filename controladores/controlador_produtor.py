from controladores.controlador_principal import ControladorPrincipal
from entidades.produtor import Produtor
from telas.tela_produtor import TelaProdutor


class ControladorProdutor:
    def __init__(self):
        self.__produtores = []
        self.__tela_produtor = TelaProdutor()
        self.__tela_aberta = False

    def inclui_produtor(self, nome, cpf, nascimento, email, celular, senha):
        produtor = Produtor(nome, cpf, nascimento, email, celular, senha)
        try:
            for i in self.__produtores:
                if produtor.cpf == i.cpf:
                    raise SystemError
            else:
                self.__produtores.append(produtor)
                self.__tela_produtor.mostrar_opcoes_produtor()
        except SystemError:
            self.__tela_produtor.usuario_ja_existe()

    def escolher_acao(self):
        self.__tela_aberta = True
        opcoes = {1: self.adicionar_evento, 2: self.editar_evento,
                  3: self.transferir_ingresso, 4: self.alterar_produtor,
                  5: self.exclui_produtor, 6: self.sair_da_conta}
        while self.__tela_aberta:
            opcao = self.__tela_produtor.mostra_tela_opcoes_pos_login()
            opcoes[opcao]()


    def retorna_produtor_pelo_cpf(self, cpf):
        for produtor in self.__produtores:
            if produtor.cpf == cpf:
                return produtor

    def alterar_produtor(self):
        pass

    def exclui_produtor(self):
        pass

    def listar_produtores(self):
        pass

    def adicionar_evento(self):
        pass

    def adicionar_venda_historico_vendas(self):
        pass

    def editar_evento(self):
        pass

    def adicionar_evento_historico_eventos(self):
        pass

    def adicionar_evento_disponivel(self):
        pass

    def remover_evento_disponivel(self):
        pass

    def excluir_conta(self):
        pass

    def transferir_ingresso(self):
        pass

    def sair_da_conta(self):
        self.__tela_aberta = False