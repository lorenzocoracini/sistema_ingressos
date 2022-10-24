from entidades.produtor import Produtor
from telas.tela_produtor import TelaProdutor


class ControladorProdutor:
    def __init__(self):
        self.__produtores = []
        self.__tela_produtor = TelaProdutor()

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

    def retorna_produtor_pelo_cpf(self, cpf):
        for produtor in self.__produtores:
            if produtor.cpf == cpf:
                return produtor

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