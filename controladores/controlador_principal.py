import sys

from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ContraladorIngressos
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_evento = ControladorEvento()
        self.__controlador_ingressos = ContraladorIngressos()
        self.__controlador_comprador = ControladorComprador()
        self.__controlador_produtor = ControladorProdutor(self)
        self.__usuario_logado = None

    def cadastro_novo_usuario(self):
        dados = self.__tela_principal.mostra_tela_cadastro()
        if (dados["tipo_cadastro"]).lower() == "produtor":
            self.__usuario_logado = self.__controlador_produtor.inclui_produtor(dados["nome"], dados["cpf"], dados["nascimento"],
                                                      dados["email"], dados["celular"], dados["senha"])
            self.__controlador_produtor.escolher_acao()



        elif (dados["tipo_cadastro"]).lower() == "comprador":
            self.__controlador_comprador.inclui_comprador(dados["nome"], dados["cpf"], dados["nascimento"],
                                                          dados["email"], dados["celular"], dados["senha"])
            self.__controlador_comprador.escolher_acao()
            self.__usuario_logado = dados['cpf']

    def login(self):
        dados_login = self.__tela_principal.mostrar_tela_login()
        comprador = self.__controlador_comprador.retorna_comprador_e_senha_pelo_cpf(dados_login["cpf"])
        produtor = self.__controlador_produtor.retorna_produtor_e_senha_pelo_cpf(dados_login["cpf"])
        if comprador:
            if dados_login["senha"] == comprador[1]:
                self.__controlador_comprador.escolher_acao()
        elif produtor:
            if dados_login["senha"] == produtor[1]:
                self.__controlador_produtor.escolher_acao()


    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.cadastro_novo_usuario, 2: self.login, 0: self.finaliza}
        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            metodo_escolihido = opcoes[opcao]
            metodo_escolihido()

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self,valor):
        self.__usuario_logado = valor

    def deslogar(self):
        self.__usuario_logado = None