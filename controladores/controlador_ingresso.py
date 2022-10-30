from entidades.ingresso import Ingresso
from entidades.comprador import Comprador
from telas.tela_ingresso import TelaIngresso


class ContraladorIngressos:
    def __init__(self):
        self.__ingressos = []
        self.__tela_ingresso = TelaIngresso()
        self.__codigo = 0

    def adicionar_ingresso(self):
        valor,lote,evento = self.__tela_ingresso.pegar_dados()
        ingresso = Ingresso(valor, self.__codigo, lote, evento)
        self.__codigo+=1
        try:
            for i in self.__ingressos:
                if ingresso.codigo == i.codigo:
                    raise Exception

            else:
                self.__ingressos.append(ingresso)

        except Exception:
            return None

    def retorna_ingresso_pelo_codigo(self,codigo):
        for ingresso in self.__ingressos:
            if ingresso.codigo == codigo:
                return ingresso

    def alterar_ingresso(self):
        nome,valor,lote,codigo,evento = self.__tela_ingresso.alterar_ingresso()
        ing = None
        for ingresso in self.__ingressos:
            if ingresso.evento == nome:
                ing = ingresso
        ing.valor = valor
        ing.codigo = codigo
        ing.lote = lote
        ing.evento = evento

    def excluir_ingresso(self):
        evento = self.__tela_ingresso.evento_para_excluir_os_ingressos()
        for ing in self.__ingressos:
            if ing.evento == evento:
                self.__ingressos.remove(ing)


    def listar_ingressos(self):
        nome = self.__tela_ingresso.evento_para_listar_os_ingressos()
        lista = []
        for ing in self.__ingressos:
            if ing.evento == nome:
                lista.append(ing)

        self.__tela_ingresso.lista_ingressos(lista)