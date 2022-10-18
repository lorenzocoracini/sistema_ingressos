from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador

class ControladorComprador:
    def __init__(self):
        self.__tela_comprador = TelaComprador()
        self.__compradores = []

    def adicionar_comprador(self):
        dados = self.__tela_comprador.pegar_dados()
        comprador = Comprador(dados["nome_comprador"], dados["cpf_comprador"], dados["nascimento_comprador"],
                              dados["email_comprador"], dados["celular_comprador"], 0)
        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
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
