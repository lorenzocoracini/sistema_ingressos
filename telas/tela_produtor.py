class TelaProdutor:
    def mostra_tela_produtor(self):
        print('*'*20)
        print("POSSUI CADASTRO ? ")
        print('1 - LOGIN')
        print('2 - CADASTRE - SE ')
        opcao = int(input('ESCOLHA A OPÇÃO: '))

        return opcao

    def mostra_tela_cadastro_produtor(self):
        print("Digite seus dados:")
        self.__nome = input("Nome: ")
        self.__cpf = int(input("CPF (Coloque apenas números):  "))
        self.__nascimento = input("Nascimento: ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))

        return {"nome_produtor": self.__nome, "cpf_produtor": self.__cpf, "nascimento_produtor": self.__nascimento,
                "email_produtor": self.__email, "celular_produtor": self.__celular}

    def mostra_tela_login_produtor(self):
        print('login produtor')
        self.__cpf_login = input("Digite seu CPF: ")
        self.__senha_login = input("Digite sua senha: ")
        dados_login_produtor = {"cpf_login_produtor": self.__cpf_login, "senha_login_produtor": self.__senha_login}
        return dados_login_produtor

    def mostra_tela_opcoes_pos_login(self):
        print("Login efetuado com sucesso")
        print("1 - Adicionar evento")
        print("2 - Editar evento")
        print("3 - Transferir ingresso")
        opcao = int(input('ESCOLHA A OPÇÃO'))
        return opcao


    def listar_dados_produtor(self):
        pass
