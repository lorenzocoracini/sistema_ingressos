class TelaEvento:
    def __init__(self, controlador_produtor):
        self.__contolador_produtor = controlador_produtor

    def pegar_dados(self):
        print("CADASTRO EVENTO")
        try:
            codigo = int(input('CODIGO: '))
            nome = str(input("NOME: "))
            dia_evento = str(input('DIA DO EVENTO: '))
            if int(dia_evento) > 31 or int(dia_evento) <= 0:
                raise ValueError
            mes_evento = str(input('MÊS DO EVENTO: '))
            if int(mes_evento) > 12 or int(mes_evento) <= 0:
                raise ValueError
            ano_evento = str(input('ANO DO EVENTO: '))
            if int(ano_evento) <= 0:
                raise ValueError
            hr_evento = str(input('HORA DO EVENTO (hora:minutos) : '))
            lista = hr_evento.split(':')
            if int(lista[0]) > 23 or int(lista[0]) < 0 or int(lista[1]) > 59 or int(lista[1]) < 0:
                raise ValueError
            descricao = str(input("DESCRIÇÃO: "))
            atracao = str(input("ATRAÇÕES: "))
            despesas = int(input("DESPESAS: "))
            rua = str(input("RUA DO LOCAL: "))
            bairro = str(input("BAIRRO DO LOCAL: "))
            cidade = str(input("CIDADE DO LOCAL: "))
            cep = int((input("CEP DO LOCAL: ")))
            lotacao_maxima = int(input("LOTAÇÃO MÁXIMA: "))
            aluguel = float(input("ALUGUEL DO LOCAL: "))

            return {'codigo_evento': codigo, 'data_evento': f'{dia_evento}/{mes_evento}/{ano_evento} {hr_evento}',
                    'nome_evento': nome, 'descricao_evento': descricao,
                    'atracao_evento': atracao, 'despesas_evento': despesas, 'rua_evento': rua, 'bairro_evento': bairro,
                    'cidade_evento': cidade, 'cep_evento': cep, 'lotacao_maxima_evento': lotacao_maxima,
                    'aluguel_evento': aluguel}

        except ValueError:
            print('Dados incorretos , preencha novamente de acordo com as instruções')
            self.__contolador_produtor.adicionar_evento()
