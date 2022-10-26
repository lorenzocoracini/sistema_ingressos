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
        print("1 - Nome")
        print("2 - CPF")
        print("3 - Nascimento")
        print("4 - Email")
        print("5 - Celular")
        print("6 - Senha")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 2 or opcao == 5:
            dado_atualizado = int(input("Digite o dado atualizado: "))
        elif opcao == 3:
            input("Digite o dado atualizado (dd/mm/aa: ")
        else:
            input("Digite o dado atualizado: ")
        return opcao, dado_atualizado
