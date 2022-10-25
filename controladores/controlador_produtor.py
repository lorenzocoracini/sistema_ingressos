from entidades.produtor import Produtor
from entidades.evento import Evento
from entidades.local import Local
from telas.tela_produtor import TelaProdutor
from telas.tela_evento import TelaEvento
from controladores.controlador_evento import ControladorEvento


class ControladorProdutor:
    def __init__(self,controlador_principal):
        self.__produtores = []
        self.__tela_produtor = TelaProdutor()
        self.__tela_evento = TelaEvento()
        self.__tela_aberta = False
        self.__controlador_principal = controlador_principal


    def inclui_produtor(self, nome, cpf, nascimento, email, celular, senha):
        produtor = Produtor(nome, cpf, nascimento, email, celular, senha)
        try:
            for i in self.__produtores:
                if produtor.cpf == i.cpf:
                    raise SystemError
            else:
                self.__produtores.append(produtor)

                return produtor
        except SystemError:
            self.__tela_produtor.usuario_ja_existe()




    def retorna_produtor_e_senha_pelo_cpf(self, cpf):
        for produtor in self.__produtores:
            if produtor.cpf == cpf:
                return [produtor,produtor.senha]


    def escolher_acao(self):
        self.__tela_aberta = True
        opcoes = {1:self.adicionar_evento, 2: self.editar_evento, 3: self.transferir_ingresso,
                  4: self.altera_dados_produtor, 5: self.exclui_produtor, 6: self.sair_da_conta}
        while self.__tela_aberta:
            opcao = self.__tela_produtor.mostrar_opcoes_produtor()
            opcoes[opcao]()


    def altera_dados_produtor(self):
        pass

    def exclui_produtor(self):
        for produtor in self.__produtores:
            if produtor.cpf == self.__controlador_principal.usuario_logado.cpf:
                self.__produtores.remove(produtor)
                break


    def listar_produtores(self):
        return self.__produtores

    def adicionar_evento(self):
        dados = self.__tela_evento.pegar_dados()
        local = Local(dados['rua_evento'],dados['bairro_evento'],dados['cidade_evento'],
                      dados['cep_evento'],dados['lotacao_maxima'],dados['aluguel'])

        evento = Evento(dados['codigo_evento'],dados['data_evento'],
                        dados['nome_evento'],dados['descricao_evento'],
                        dados['atracao_evento'],dados['despesas_evento'],local)
        """
        try:
            for i in :
                if produtor.cpf == i.cpf:
                    raise SystemError
            else:
                self.__produtores.append(produtor)

                return produtor
        except SystemError:
            self.__tela_produtor.usuario_ja_existe()
        """


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

    def editar_evento(self):
        pass

    def transferir_ingresso(self):
        pass

    def sair_da_conta(self):
        self.__tela_aberta = False
        self.__controlador_principal.deslogar()
