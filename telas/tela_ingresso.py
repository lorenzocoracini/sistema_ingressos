class TelaIngresso:

    def pegar_dados(self):
        print('DADOS INGRESSOS')
        valor = float(input('Digite o valor do ingresso: '))
        lote = int(input('Digite o lote do ingresso: '))
        evento = input('Digite o evento do ingresso: ')
        return {'valor_do_ingresso': valor,
                'lote_do_ingresso': lote,
                'evento_do_ingresso': evento}

    def alterar_ingresso(self):
        nome = str(input('Digite o nome do evento dos ingressos que deseja altera:'))
        print('DIGITE OS NOVOS DADOS PARA O INGRESSO:')
        valor = float(input('Digite o  valor do ingresso: '))
        lote = int(input('Digite o  lote do ingresso: '))
        codigo = int(input('Digite o o código do ingresso: '))
        evento = input('Digite o evento do ingresso: ')
        return {'nome':nome,
                'valor_do_ingresso': valor,
                'lote_do_ingresso': lote,
                'codigo_do_ingresso':codigo,
                'evento_do_ingresso': evento}

    def evento_para_excluir_os_ingressos(self):
        nome = str(input('Digite o nome do evnto que deseja exlcuir os ingressos:'))
        return nome

    def evento_para_listar_os_ingressos(self):
        nome = str(input('Digite o nome do evento que deseja listar'))
        return nome

    def lista_ingressos(self,lista_de_ingressos):
        lista = lista_de_ingressos
        for ing in lista:
            print(ing)
