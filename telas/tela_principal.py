import PySimpleGUI as sg

'''
class TelaPrincipal2:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def pega_opcao(self):
        self.init_opcoes()
        button, values = self.__window.open()
        if button == 'Login':
            self.tela_login()
        else:
            self.tela_cadastro()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text('Bem-vindo ao tickets.com', size=(40, 2))],
            [sg.Button('Registre-se')],
            [sg.Button('Login')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)

    def tela_login(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Login")],
            [sg.Text("Digite seus dados:")],
            [sg.Text("Cpf", size=(15, 1)), sg.InputText(key='input_cpf')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)

    def tela_cadastro(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Cadastre-se")],
            [sg.Text("Digite seus dados:")],
            [sg.Text("Nome", size=(15, 1)), sg.InputText(key='input_nome')],
            [sg.Text("Cpf", size=(15, 1)), sg.InputText(key='input_cpf')],
            [sg.Text("Dia do nascimento", size=(15, 1)), sg.InputText(key='input_dia_nascimento')],
            [sg.Text("Mes do nascimento", size=(15, 1)), sg.InputText(key='input_mes_nascimento')],
            [sg.Text("Ano do nascimento", size=(15, 1)), sg.InputText(key='input_ano_nascimento')],
            [sg.Text("Email", size=(15, 1)), sg.InputText(key='input_email')],
            [sg.Text("Celular", size=(15, 1)), sg.InputText(key='input_celular')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Text("Como voce deseja se cadastrar?")],
            [sg.Button("Comprador"), sg.Button("Produtor")],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        print(button)
        print(values)
        return button, values

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()


TelaPrincipal2().open()

'''
class TelaPrincipal:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal

    def mostra_tela_inicial(self):
        print('*' * 20)
        print('PRIMEIRA VEZ NO APLICATIVO?')
        print('1 - Registre-se')
        print('2 - Login ')
        print('0 - SAIR')
        try:
            opcao = int(input('ESCOLHA A OPÇÃO: '))
            if isinstance(opcao, int) and 0 <= opcao <= 2:
                return opcao
            else:
                raise ValueError
        except ValueError:
            print("A opção digitada não é válida, digite novamente.")
            self.__controlador_principal.inicia()

    def mostra_tela_cadastro(self):
        print("*" * 20)
        print("Digite seus dados:")
        print("*" * 20)
        while True:
            try:
                self.__nome = input("Nome: ")
                self.__cpf = int(input("CPF (Coloque apenas números):  "))
                dia_nascimento = int(input("Digite o dia do seu nascimento: "))
                mes_nascimento = int(input("Digite o número correspondente ao mês do seu nascimento: "))
                ano_nascimento = int(input("Digite o ano do seu nascimento: "))
                if not self.__controlador_principal.verificar_data(dia_nascimento, mes_nascimento, ano_nascimento):
                    raise ValueError
                self.__email = input("Email: ")
                self.__celular = int(input("Celular (Coloque apenas números): "))
                self.__senha = input("Senha:")
                self.__tipo = int(input("Forma de cadastro (Digite o número: 1 - Comprador ou 2 - Produtor): "))
                return {"nome": self.__nome, "cpf": self.__cpf,
                        "nascimento": f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}",
                        "email": self.__email, "celular": self.__celular, "senha": self.__senha,
                        "tipo_cadastro": self.__tipo}

            except ValueError:
                print("Dados errados, favor inserir os dados segundo as instruções.")

    def mostrar_tela_login(self):
        print("*" * 20)
        print("Digite seus dados:")
        print("*" * 20)
        while True:
            try:
                self.__cpf_login = int(input("CPF: "))
                self.__senha_login = input("SENHA:")
                return {"cpf": self.__cpf_login, "senha": self.__senha_login}
            except ValueError:
                print("Dados errados, favor inserir os dados segundo as instruções.")

    def acao_realizada(self):
        print(" A ação foi realizada com sucesso!")

    def credenciais_incorretas(self):
        print("A senha digitada não confere com o cpf.")

    def nao_existe_conta(self):
        print("Não existe uma conta cadastrada com esse CPF.")

    def cpf_em_uso(self):
        print("O cpf já está vinculado à outra conta")
