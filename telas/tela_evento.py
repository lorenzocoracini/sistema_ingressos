from datetime import datetime


class TelaEvento:
    def __init__(self,controlador_produtor):
        self.__contolador_produtor = controlador_produtor

    def pegar_dados(self):
        print("CADASTRO EVENTO")
        try:
            codigo = int(input('CODIGO: '))
            nome = str(input("NOME: "))
            data = str(input('DATA (dd/mm/aaaa hh:mm)'))
            descricao = str(input("DESCRIÇÃO: "))
            atracao = str(input("ATRAÇÕES: "))
            despesas = int(input("DESPESAS: "))
            rua = str(input("RUA DO LOCAL: "))
            bairro = str(input("BAIRRO DO LOCAL: "))
            cidade = str(input("CIDADE DO LOCAL: "))
            cep = int((input("CEP DO LOCAL: ")))
            lotacao_maxima = int(input("LOTAÇÃO MÁXIMA: "))
            aluguel = float(input("ALUGUEL DO LOCAL: "))

            return {'codigo_evento': codigo, 'data_evento': data, 'nome_evento': nome, 'descricao_evento': descricao,
                    'atracao_evento': atracao, 'despesas_evento': despesas, 'rua_evento': rua, 'bairro_evento': bairro,
                    'cidade_evento': cidade, 'cep_evento': cep, 'lotacao_maxima_evento': lotacao_maxima,
                    'aluguel_evento': aluguel}

        except ValueError:
            print('Dados incorretos , preencha novamente de acordo com as instruções')
            self.__contolador_produtor.adicionar_evento()




