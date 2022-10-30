class TelaProdutor:
    def __init__(self, controlador_produtor):
        self.__controlador_produtor = controlador_produtor

    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido.")

    def mostrar_opcoes_produtor(self):
        print("1 - Adicionar evento")
        print("2- Ver meus eventos")
        print("3 - Editar evento")
        print('4 - Excluir evento')
        print('5 - Histórico de eventos')
        print('6 - Excluir conta')
        print('7 - Sair da conta')
        try:
            opcao = int(input("Digite a opcao desejada:"))
            if isinstance(opcao, int) and 1 <= opcao <= 7:
                return opcao
            else:
                raise ValueError
        except ValueError:
            print("A opcão digitada não é válida, digite um número dentre as opcções abaixo")
            self.__controlador_produtor.escolher_acao()

    def alterar_evento(self):
        while True:
            try:
                codigo_evento = int(input('Digite o código do evento que deseja editar:'))
                print("Preencha os dados atualizados:")
                codigo = int(input('CODIGO: '))
                dia_evento = str(input('DIA DO EVENTO: '))
                if int(dia_evento)> 31 or int(dia_evento)<= 0:
                    raise ValueError
                mes_evento = str(input('MÊS DO EVENTO: '))
                if int(mes_evento)>12 or int(mes_evento)<=0:
                    raise ValueError
                ano_evento = str(input('ANO DO EVENTO: '))
                if int(ano_evento)<=0:
                    raise ValueError
                hr_evento = str(input('HORA DO EVENTO (hora:minutos) : '))
                lista = hr_evento.split(':')
                if int(lista[0]) >23 or int(lista[0])<0 or int(lista[1])>59 or int(lista[1])<0:
                    raise ValueError
                nome = str(input("NOME: "))
                descricao = str(input("DESCRIÇÃO: "))
                atracao = str(input("ATRAÇÕES: "))
                despesas = int(input("DESPESAS: "))

                dados_atualizados = {'codigo_evento': codigo,
                                     'data_evento': f'{dia_evento}/{mes_evento}/{ano_evento} {hr_evento}',
                                     'nome_evento': nome,
                                     'descricao_evento': descricao,
                                     'atracao_evento': atracao, 'despesas_evento': despesas}
                return codigo_evento, dados_atualizados

            except ValueError:
                print('Dados preenchidos incorretamente')



    def remover_evento(self):
        print('Exclusão de evento')
        codigo = int(input("Digite o código do evento a ser excluído:"))
        return codigo

    def mostar_eventos(self, eventos):
        for evento in eventos:
            print(evento.nome)

    def mostar_historico_de_eventos(self, eventos):
        lista_eventos = eventos
        print("Histórico de eventos")
        for evento in lista_eventos:
            for nome, data in evento.items():
                print('NOME: ', nome)
                print('DATA: ', data)

    def deu_erro(self):
        print('deu erro')

    def listar_dados_produtor(self):
        pass
