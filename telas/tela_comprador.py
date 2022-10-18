class TelaComprador:
    def mostra_opcoes(self):
        pass

    def pegar_dados(self):
        print("Digite seus dados:")
        self.__nome = input("Nome: ")
        self.__cpf = int(input("CPF (Coloque apenas números):  "))
        self.__nascimento = input("Nascimento: ")
        self.__email = input("Email: ")
        self.__celular = int(input("Celular (Coloque apenas números): "))
        return {"nome_comprador": self.__nome, "cpf_comprador": self.__cpf, "nascimento_comprador": self.__nascimento,
                "email_comprador": self.__email, "celular_comprador": self.__celular}

    def listar_dados_comprador(self):
        pass