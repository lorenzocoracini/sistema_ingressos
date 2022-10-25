class TelaEvento:
    def mostar_opcoes(self):
        print('*' * 20)
        print("EVENTOS")
        print("*" * 20)
        print('1 - Adicionar Evento')
        print('2 - Excluir Evento')
        print('3 - Listar Evento')
        print('4 - Alterar Evento')
        print('0 - Voltar')
        opcao = int(input('Digite a opção'))
        return opcao

    def pegar_dados(self):
        print("CADASTRO EVENTO")
        codigo = int(input('CODIGO: '))
        data = str(input('DATA: '))
        nome = str(input("NOME: "))
        descricao = str(input("DESCRIÇÃO: "))
        atracao = str(input("ATRAÇÕES: "))
        despesas = int(input("DESPESAS: "))
        # ingressos = int(input("INGRESSOS: "))
        rua = str(input("RUA DO LOCAL: "))
        bairro = str(input("BAIRRO DO LOCAL: "))
        cidade = str(input("CIDADE DO LOCAL: "))
        cep = int((input("CEP DO LOCAL: ")))
        lotacao_maxima = int(input("LOTAÇÃO MÁXIMA: "))
        aluguel = float(input("ALUGUEL DO LOCAL: "))

        return {'codigo_evento': codigo, 'data_evento': data, 'nome_evento': nome, 'descricao_evento': descricao,
                'atracao_evento': atracao, 'despesas_evento': despesas, 'rua_evento': rua, 'bairro_evento': bairro,
                'cidade_evento': cidade, 'cep_evento': cep, 'lotacao_maxima_evento': lotacao_maxima, 'alugel': aluguel}

    def listar_dados_eventos(self):
        pass
