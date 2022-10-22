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
        self.__cpf = int(input("CPF (Coloque apenas números): "))
        self.__nascimento = input("Nascimento: ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))
        self.__senha = input("Senha: ")

        return {"nome_comprador": self.__nome, "cpf_comprador": self.__cpf, "nascimento_comprador": self.__nascimento,
                "email_comprador": self.__email, "celular_comprador": self.__celular, "senha_comprador": self.__senha}

    def mostra_tela_login_comprador(self):
        print('login comprador')
        self.__cpf_login = input("Digite seu CPF: ")
        self.__senha_login = input("Digite sua senha: ")
        return {"cpf_login_comprador": self.__cpf_login, "senha_login_comprador": self.__senha_login}

    def deu_erro(self):
        print("Os dados fornecidos estão errados!")

    def mostra_opcoes_pos_login(self):
        print("Login efetuado com sucesso!")
        print("1 - Pesquisar Evento")
        print("2 - Ver meus ingressos")
        print("3 - Ver eventos disponíveis")
        print("4 - Favoritar Evento")
        print("5 - Editar meus dados")
        print("6 - Transferir ingresso")
        opcao = input("Digite a opcao desejada:")
        return opcao

    def listar_dados_comprador(self):
        pass