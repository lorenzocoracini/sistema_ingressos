from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador

class ControladorComprador:
    def __init__(self):
        self.__tela_comprador = TelaComprador()
        self.__compradores = []

    def adicionar_comprador(self):
        dados = self.__tela_comprador.mostra_tela_cadastro_comprador()
        comprador = Comprador(dados["nome_comprador"], dados["cpf_comprador"], dados["nascimento_comprador"],
                              dados["email_comprador"], dados["celular_comprador"], 0)
        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
                self.__tela_comprador.mostrar_opcoes_comprador()
        except SystemError:
            return None

    def alterar_comprador(self):
        pass

    def excluir_comprador(self):
        pass

    def listar_compradores(self):
        pass

    def comprar_ingresso(self):
        pass

    def verificar_login(self):
        dados_login = self.__tela_comprador.mostra_tela_login_comprador()
        comprador_fazendo_login = None
        for comprador in self.__compradores:
                if comprador.cpf == dados_login["cpf_login_comprador"]:
                    comprador_fazendo_login = comprador
                if comprador_fazendo_login.senha == dados_login["senha_login_comprador"]:
                    self.__tela_comprador.mostrar_opcoes_comprador()
                else:
                    self.__tela_comprador.teste_errado()