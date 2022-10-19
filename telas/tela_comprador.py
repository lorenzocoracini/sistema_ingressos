class TelaComprador:
    def mostra_tela_comprador(self):
        print('*'*20)
        print("POSSUI CADASTRO ? ")
        print('1 - LOGIN')
        print('2 - CADASTRE - SE ')
        opcao = int(input('ESCOLHA A OPÇÃO: '))

        return opcao

    def mostra_tela_cadastro_comprador(self):
        print("Digite seus dados:")
        self.__nome = input("Nome: ")
        self.__cpf = int(input("CPF (Coloque apenas números):  "))
        self.__nascimento = input("Nascimento: ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))

        return {"nome_comprador": self.__nome, "cpf_comprador": self.__cpf, "nascimento_comprador": self.__nascimento,
                "email_comprador": self.__email, "celular_comprador": self.__celular}

    def mostra_tela_login_comprador(self):
        print('login produtor')


    def listar_dados_comprador(self):
        pass