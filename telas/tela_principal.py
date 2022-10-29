class TelaPrincipal:

    def mostra_tela_inicial(self):
        print('*' * 20)
        print('PRIMEIRA VEZ NO APLICATIVO?')
        print('1 - Registre-se')
        print('2 - Login ')
        print('0 - SAIR')
        opcao = int(input('ESCOLHA A OPÇÃO: '))
        return opcao

    def mostra_tela_cadastro(self):
        print("Digite seus dados:")
        self.__nome = input("Nome: ")
        self.__cpf = int(input("CPF (Coloque apenas números):  "))
        self.__nascimento = input("Nascimento (DD/MM/AA): ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))
        self.__senha = input("Senha:")
        self.__tipo = int(input("Forma de cadastro (Digite o número: 1 - Comprador ou 2 - Produtor): "))
        return {"nome": self.__nome, "cpf": self.__cpf, "nascimento": self.__nascimento,
                "email": self.__email, "celular": self.__celular,"senha": self.__senha, "tipo_cadastro":self.__tipo}

    def mostrar_tela_login(self):
        print("Digite seus dados:")
        self.__cpf_login = int(input("CPF: "))
        self.__senha_login = input("SENHA:")
        return {"cpf": self.__cpf_login, "senha": self.__senha_login}

    def acao_realizada(self):
        print(" A ação foi realizada com sucesso!")