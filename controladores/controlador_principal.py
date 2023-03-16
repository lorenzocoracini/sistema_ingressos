import sys
from controladores.controlador_comprador import ControladorComprador
from controladores.controlador_evento import ControladorEvento
from controladores.controlador_ingresso import ControladorIngresso
from controladores.controlador_produtor import ControladorProdutor
from telas.tela_principal import TelaPrincipal
from exceptions.cpfNotFoundException import CpfNotFoundException


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_ingressos = ControladorIngresso(self)
        self.__controlador_evento = ControladorEvento(self.__controlador_ingressos)
        self.__controlador_comprador = ControladorComprador(self, self.__controlador_evento, self.__controlador_ingressos)
        self.__controlador_produtor = ControladorProdutor(self, self.__controlador_evento)
        self.__tela_principal = TelaPrincipal()
        self.__usuario_logado = None

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado

    @property
    def controlator_evento(self):
        return self.__controlador_evento

    @property
    def controlador_ingressos(self):
        return self.__controlador_ingressos

    @property
    def controlator_comprador(self):
        return self.__controlador_comprador

    @property
    def controlator_produtor(self):
        return self.__controlador_produtor

    @property
    def tela_principal(self):
        return self.__tela_principal

    def inicializa_sistema(self):
        opcao = self.__tela_principal.escolher_login_ou_cadastro()
        if opcao == "Login":
            self.trata_login()
        elif opcao == "Registre-se":
            self.trata_cadastro()
        else:
            self.finaliza()

    def trata_cadastro(self):
        deu_certo = False
        while not deu_certo:
            button, values = self.__tela_principal.tela_cadastro()
            if button == "Cancel":
                deu_certo = True
                self.inicializa_sistema()
            elif button is None:
                self.__tela_principal.mostra_mensagem("Os dados fornecidos estão incorretos, favor inserir novamente.")
            else:
                if button == 'Comprador':
                    self.__controlador_comprador.inclui_comprador(values)

                elif button == 'Produtor':
                    self.__controlador_produtor.inclui_produtor(values)

    def trata_login(self):
        deu_certo = False

        while not deu_certo:

            button, values = self.__tela_principal.tela_login()

            if button == 'Cancel':
                deu_certo = True
                self.inicializa_sistema()
            elif button is None and values is None:
                self.__tela_principal.mostra_mensagem("Os dados fornecidos estão incorretos, favor inserir novamente.")
            else:
                try:
                    comprador = self.__controlador_comprador.retorna_comprador_pelo_cpf(values['input_cpf'])
                    produtor = self.__controlador_produtor.retorna_produtor_pelo_cpf(values['input_cpf'])

                    if comprador:
                        if values['input_senha'] == comprador.senha:
                            self.__usuario_logado = comprador
                            deu_certo = True
                            self.__usuario_logado = comprador
                            self.__controlador_comprador.mostrar_opcoes_comprador()

                        else:
                            self.__tela_principal.mostra_mensagem(
                                "A senha cadastrada não confere com o cpf inserido. Tente Novamente.")

                    elif produtor:
                        if values['input_senha'] == produtor.senha:
                            self.__usuario_logado = produtor
                            deu_certo = True
                            self.__usuario_logado = produtor
                            self.__controlador_produtor.mostrar_opcoes_produtor()
                        else:
                            self.__tela_principal.mostra_mensagem(
                                "A senha cadastrada não confere com o cpf inserido. Tente Novamente.")
                    else:
                        raise CpfNotFoundException()
                except CpfNotFoundException:
                    self.__tela_principal.mostra_mensagem("Não existe uma conta cadastrada com esse cpf.")


    def altera_usuario_logado(self, usuario):
        self.__usuario_logado = usuario

    def deslogar(self):
        self.__usuario_logado = None

    def finaliza(self):
        sys.exit()