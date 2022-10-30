class TelaIngresso:

    def pegar_dados(self):
        print('DADOS INGRESSOS')
        valor = float(input('Digite o valor do ingresso: '))
        lote = int(input('Digite o lote do ingresso: '))
        evento = input('Digite o evento do ingresso: ')
        return {'valor_do_ingresso': valor,
                'lote_do_ingresso': lote,
                'evento_do_ingresso': evento}

    def pegar_dados_para_transferencia_do_ingresso(self):
        codigo = int(input('Digite o código do ingresso que será transferiado: '))
        cpf_que_vai_receber_ingresso = int(input('Digite o cpf de quem vai receber o ingresso'))

        return codigo, cpf_que_vai_receber_ingresso
