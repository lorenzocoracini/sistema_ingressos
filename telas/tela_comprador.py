class TelaComprador:
    def mostrar_opcoes_comprador(self):
        print("*"*20)
        print("1 - Ver meus ingressos")
        print("2 - Ver eventos disponíveis")
        print("3 - Ver eventos Favoritos")
        print("4 - Favoritar Evento")
        print("5 - Transferir ingresso")
        print("6 - Editar meus dados")
        print("7 - Excluir Conta")
        print("8 - Sair da Conta")
        opcao = input("Digite a opcao desejada:")
        return int(opcao)

    def deu_erro(self):
        print("Os dados fornecidos estão errados!")

    def listar_dados_comprador(self, comprador_logado):
        print("Nome: ", comprador_logado.nome)
        print("CPF: ", comprador_logado.cpf)
        print("Nascimento: ", comprador_logado.nascimento)
        print("Email: ", comprador_logado.email)
        print("Celular: ", comprador_logado.celular)
        print("Senha: ", comprador_logado.senha)

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
            dado_atualizado = input("Digite o dado atualizado (dd/mm/aa): ")
        else:
            dado_atualizado = input("Digite o dado atualizado: ")
        return opcao, dado_atualizado

    def mostrar_meus_ingressos(self, ingressos):
        for ingresso in ingressos:
            print(ingresso)

    def pegar_dados_para_favoritar_evento(self):
        print()

    def mostrar_eventos_favoritos(self, eventos_favoritos):
        for evento in eventos_favoritos:
            print(evento.nome)

    def pegar_dados_transferir_ingresso(self):
        print("Dados para a tranferência de ingresso:")
        cpf = int(input("Digite o cpf da pessoa:"))
        nome_do_evento = input("Digite o nome do evento: ")
        codigo_do_ingresso= int(input("Digite o código do ingresso a ser transferido: "))
        return cpf, nome_do_evento, codigo_do_ingresso