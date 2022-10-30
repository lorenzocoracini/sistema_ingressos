class TelaProdutor:
    def __init__(self,controlador_produtor):
        self.__controlador_produtor = controlador_produtor


    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido.")

    def mostrar_opcoes_produtor(self):
        print("1 - Adicionar evento")
        print("2- Ver meus eventos")
        print("3 - Editar evento")
        print('4 - Excluir evento')
        print('5 - Editar meus dados')
        print('6 - Histórico de eventos')
        print('7 - Excluir conta')
        print('8 - Sair da conta')
        try:
            opcao = int(input("Digite a opcao desejada:"))
            if isinstance(opcao, int) and 1 <= opcao <= 8:
                return opcao
            else:
                raise ValueError
        except ValueError:
            print("A opcão digitada não é válida, digite um número dentre as opcções abaixo")
            self.__controlador_produtor.escolher_acao()


    def alterar_evento(self):
        print("Escolha dado que deseja alterar:")
        print('1 - Codigo')
        print('2 - Data')
        print('3 - Nome')
        print('4 - Descrição')
        print('5 - Atrações')
        print('6 - Despesas')
        codigo_evento = int(input('Digite o código do evento que deseja editar:'))
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 2:
            dado_atualizado = input("Digite a data do evento atualizado (dd/mm/aa %h:%m):")
        elif opcao == 1:
            dado_atualizado = int(input('Digite o codigo atualizado: '))
        elif opcao == 6:
            dado_atualizado = float(input('Digite as despesas atualizadas: '))
        else:
            dado_atualizado = input('Digite o dado atualizado')
        return codigo_evento, opcao, dado_atualizado

    def escolher_dado_para_alterar(self):
        print("Escolha qual dado que deseja alterar:")
        print("1 - Nome")
        print("2 - CPF")
        print("3 - Nascimento")
        print("4 - Email")
        print("5 - Celular")
        print("6 - Senha")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 2 or opcao == 5:
            dado_atualizado = int(input("Digite o dado atualizado: "))
        elif opcao == 3:
            dado_atualizado = input("Digite a data de  atualizado (dd/mm/aa): ")
        else:
            dado_atualizado = input("Digite o dado atualizado: ")
        return opcao, dado_atualizado

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
