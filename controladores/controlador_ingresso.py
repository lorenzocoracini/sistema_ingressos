from entidades.ingresso import Ingresso
from entidades.comprador import Comprador


class ContraladorIngressos:
    def __init__(self):
        self.__ingressos = []

    def adicionar_ingresso(self, valor: float, codigo: int, lote: int, comprador: Comprador):
        ingresso = Ingresso(valor, codigo, lote, comprador)

        try:
            for i in self.__ingressos:
                if ingresso.codigo == i.codigo:
                    raise Exception

            else:
                self.__ingressos.append(ingresso)

        except Exception:
            return None


    def alterar_ingresso(self):
        pass

    def excluir_ingresso(self):
        pass

    def excluir_ingresso(self):
        pass

    def listar_ingressos(self):
        pass
