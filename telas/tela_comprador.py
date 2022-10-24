class TelaComprador:
    def mostrar_opcoes_comprador(self):
        print("Login efetuado com sucesso!")
        print("1 - Ver meus ingressos")
        print("2 - Ver eventos disponíveis")
        print("3 - Favoritar Evento")
        print("4 - Transferir ingresso")
        print("5 - Editar meus dados")
        print("6 - Excluir Conta")
        print("7 - Sair da Conta")
        opcao = input("Digite a opcao desejada:")
        return int(opcao)

    def deu_erro(self):
        print("Os dados fornecidos estão errados!")

    def listar_dados_comprador(self):
        pass

    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido.")

    def escolher_dado_para_alterar(self):
        print("Escolha qual dado quer alterar:")
