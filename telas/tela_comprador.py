class TelaComprador:
    def mostrar_opcoes_comprador(self):
        print("Login efetuado com sucesso!")
        print("1 - Pesquisar Evento")
        print("2 - Ver meus ingressos")
        print("3 - Ver eventos disponíveis")
        print("4 - Favoritar Evento")
        print("5 - Editar meus dados")
        print("6 - Transferir ingresso")
        opcao = input("Digite a opcao desejada:")
        return opcao

    def deu_erro(self):
        print("Os dados fornecidos estão errados!")

    def listar_dados_comprador(self):
        pass

    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido.")