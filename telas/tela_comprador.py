import PySimpleGUI as sg

'''
class TelaComprador2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text('Área do Comprador', size=(40, 2))],
            [sg.Button('Ver meus ingressos')],
            [sg.Button('Ver eventos disponíveis')],
            [sg.Button('Ver eventos favoritos')],
            [sg.Button('Favoritar evento')],
            [sg.Button('Remover evento dos favoritos')],
            [sg.Button('Comprar ingresso')],
            [sg.Button('Excluir conta')],
            [sg.Button('Sair da conta')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()


TelaComprador2().open()

'''
class TelaComprador:
    def __init__(self, controlador_comprador):
        self.__controlador_comprador = controlador_comprador

    def mostrar_opcoes_comprador(self):
        print("*" * 20)
        print("1 - Ver meus ingressos")
        print("2 - Ver eventos disponíveis")
        print("3 - Ver eventos Favoritos")
        print("4 - Favoritar Evento")
        print("5 - Remover evento dos favoritos")
        print("6 - Comprar Ingresso")
        print("7 - Excluir Conta")
        print("8 - Sair da Conta")
        try:
            opcao = int(input("Digite a opcao desejada:"))
            if isinstance(opcao, int) and 1 <= opcao <= 8:
                return opcao
            else:
                raise ValueError
        except ValueError:
            print("A opcão digitada não é válida, digite um número dentre as opcções abaixo")
            self.__controlador_comprador.escolher_acao()

    def listar_dados_comprador(self, comprador_logado):
        print("Nome: ", comprador_logado.nome)
        print("CPF: ", comprador_logado.cpf)
        print("Nascimento: ", comprador_logado.nascimento)
        print("Email: ", comprador_logado.email)
        print("Celular: ", comprador_logado.celular)
        print("Senha: ", comprador_logado.senha)

    def mostrar_meus_ingressos(self, ingressos):
        for ingresso in ingressos:
            print('Evento: ', ingresso.evento)
            print('Valor: ', ingresso.valor)

    def pegar_dados_para_favoritar_evento(self):
        print("Favoritar Evento")
        while True:
            try:
                codigo = int(input("Digite o cógido do evento a ser favoritado: "))
                return codigo
                break
            except ValueError:
                self.deu_erro()

    def mostrar_eventos_favoritos(self, eventos_favoritos):
        for evento in eventos_favoritos:
            print('Evento: ', evento.nome)
            print('Código: ', evento.codigo)
            print('Valor: ', evento.ingressos[0].valor)

    def mostrar_eventos_disponiveis(self, eventos_disponiveis):
        for evento in eventos_disponiveis:
            print("*" * 20)
            print("Nome: ", evento.nome)
            print("Código: ", evento.codigo)
            print("Data: ", evento.data)
            print("Descrição: ", evento.descricao)
            print("Atrações: ", evento.atracao)
            print("Valor do ingresso: ", evento.ingressos[0].valor)

    def pegar_evento_para_compra(self):
        evento = input('Digite o nome do evento que você deseja comprar: ')
        return evento

    def pega_evento_remover_favoritos(self):
        while True:
            try:
                codigo = int(input("Digite o código do evento que deseja remover dos favoritos:"))
                return codigo
                break
            except ValueError:
                print("O código fornecido não é válido")

    def deu_erro(self):
        print("Os dados fornecidos estão errados!")

    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido ou digite outro cpf.")
        self.__controlador_comprador.comprador_ja_existe()

    def evento_nao_existe(self):
        print("O evento inserido não existe.")
