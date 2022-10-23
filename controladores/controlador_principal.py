import sys

from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ContraladorIngressos
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal
from telas.tela_produtor import TelaProdutor
from telas.tela_comprador import TelaComprador


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_evento = ControladorEvento()
        self.__controlador_ingressos = ContraladorIngressos()
        self.__controlador_comprador = ControladorComprador()
        self.__controlador_produtor = ControladorProdutor()

    def cadastro_novo_usuario(self):
        dados = self.__tela_principal.mostra_tela_cadastro()
        if (dados["tipo_cadastro"]).lower() == "produtor":
            self.__controlador_produtor.inclui_produtor(dados["nome"], dados["cpf"], dados["nascimento"],
                                                        dados["email"], dados["celular"], dados["senha"])
        elif (dados["tipo_cadastro"]).lower() == "comprador":
            self.__controlador_comprador.inclui_comprador(dados["nome"], dados["cpf"], dados["nascimento"],
                                                          dados["email"], dados["celular"], dados["senha"])

    def login(self):
        dados_login = self.__tela_principal.mostrar_tela_login()
        if self.__controlador_comprador.retorna_comprador_pelo_cpf(dados_login["cpf"]):
            pass
        elif self.__controlador_produtor.retorna_produtor_pelo_cpf(dados_login["cpf"]):
            pass

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.cadastro_novo_usuario, 2: self.login, 0: self.finaliza}

        opcao = self.__tela_principal.mostra_tela_inicial()
        metodo_escolihido = opcoes[opcao]
        metodo_escolihido()
