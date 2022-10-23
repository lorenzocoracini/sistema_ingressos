from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self):
        self.__tela_comprador = TelaComprador()
        self.__compradores = []

    def inclui_comprador(self, nome, cpf, nascimento, email, celular, senha):
        comprador = Comprador(nome, cpf, nascimento, email, celular, senha)
        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
                self.__tela_comprador.mostrar_opcoes_comprador()
        except SystemError:
            self.__tela_comprador.usuario_ja_existe()

    def retorna_comprador_pelo_cpf(self, cpf):
        for comprador in self.__compradores:
            if comprador.cpf == cpf:
                return comprador

    def alterar_comprador(self):
        pass

    def excluir_comprador(self):
        pass

    def listar_compradores(self):
        pass

    def transferir_ingresso(self):
        pass

    def excluir_conta(self):
        pass