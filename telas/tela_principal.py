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
        print("Digite seus dados:")
        while True:
            try:
                self.__nome = input("Nome: ")
                self.__cpf = int(input("CPF (Coloque apenas números):  "))
                dia_nascimento = int(input("Digite o dia do seu nascimento: "))
                if dia_nascimento <= 0 or dia_nascimento > 31:
                    raise ValueError
                mes_nascimento = int(input("Digite o número correspondente ao mês do seu nascimento: "))
                if mes_nascimento > 12 or mes_nascimento <= 0:
                    raise ValueError
                ano_nascimento = int(input("Digite o ano do seu nascimento: "))
                self.__email = input("Email: ")
                self.__celular = int(input("Celular (Coloque apenas números): "))
                self.__senha = input("Senha:")
                self.__tipo = int(input("Forma de cadastro (Digite o número: 1 - Comprador ou 2 - Produtor): "))
                return {"nome": self.__nome, "cpf": self.__cpf, "nascimento": f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}",
                        "email": self.__email, "celular": self.__celular,"senha": self.__senha, "tipo_cadastro":self.__tipo}

            except ValueError:
                print("Dados errados, favor inserir os dados segundo as instruções.")

    def mostrar_tela_login(self):
        print("Digite seus dados:")
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