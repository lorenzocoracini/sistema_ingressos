import datetime
import sys

from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ContraladorIngressos
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal
from telas.tela_ingresso import TelaIngresso


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__tela_ingresso = TelaIngresso()
        self.__controlador_evento = ControladorEvento()
        self.__controlador_ingressos = ContraladorIngressos()
        self.__controlador_comprador = ControladorComprador(self)
        self.__controlador_produtor = ControladorProdutor(self)
        self.__usuario_logado = None
        self.__eventos_disponiveis = []


    def cadastro_novo_usuario(self):
        dados = self.__tela_principal.mostra_tela_cadastro()
        if dados["tipo_cadastro"] == 2:
            self.__usuario_logado = self.__controlador_produtor.inclui_produtor(dados["nome"], dados["cpf"], dados["nascimento"],
                                                      dados["email"], dados["celular"], dados["senha"])
            self.__tela_principal.acao_realizada()
            self.__controlador_produtor.escolher_acao()
        elif dados["tipo_cadastro"] == 1:
            self.__usuario_logado = self.__controlador_comprador.inclui_comprador(dados["nome"], dados["cpf"], dados["nascimento"],
                                                          dados["email"], dados["celular"], dados["senha"])
            self.__tela_principal.acao_realizada()
            self.__controlador_comprador.escolher_acao()


    def login(self):
        dados_login = self.__tela_principal.mostrar_tela_login()
        comprador = self.__controlador_comprador.retorna_comprador_e_senha_pelo_cpf(dados_login["cpf"])
        produtor = self.__controlador_produtor.retorna_produtor_e_senha_pelo_cpf(dados_login["cpf"])
        if comprador:
            if dados_login["senha"] == comprador[1]:
                self.__usuario_logado = comprador[0]
                self.__tela_principal.acao_realizada()
                self.__controlador_comprador.escolher_acao()
        elif produtor:
            if dados_login["senha"] == produtor[1]:
                self.__usuario_logado = produtor[0]
                self.__tela_principal.acao_realizada()
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
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado

    def deslogar(self):
        self.__usuario_logado = None

    @property
    def eventos_disponiveis(self):
        return self.__eventos_disponiveis

    @eventos_disponiveis.setter
    def eventos_disponiveis(self, evento):
        self.__eventos_disponiveis = evento

    def atualizar_eventos_disponiveis(self):
        self.__eventos_disponiveis = []
        for evento in self.__controlador_produtor.eventos:
            if evento.data >= datetime.datetime.today():
                self.__eventos_disponiveis.append(evento)

