class TelaIngresso:

    def pegar_dados(self):
        print('DADOS INGRESSOS')
        valor = float(input('Digite o valor do ingresso: '))
        lote = int(input('Digite o lote do ingresso: '))
        return {'valor_do_ingresso': valor,
                'lote_do_ingresso': lote}
