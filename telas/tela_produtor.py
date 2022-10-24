class TelaProdutor:
    def mostrar_opcoes_produtor(self):
        print("*"*20)
        print("Vão ser mostradas as opcoes")

    def usuario_ja_existe(self):
        print("O usuário já existe, faça login com o cpf fornecido.")

    def mostra_tela_opcoes_pos_login(self):
        print("Login efetuado com sucesso")
        print("1 - Adicionar evento")
        print("2 - Editar evento")
        print("3 - Transferir ingresso")
        print('4 - Editar meus dados')
        print('5 - Excluir conta')
        print('6 - Sair da conta')
        opcao = int(input('ESCOLHA A OPÇÃO'))
        return opcao

    def deu_erro(self):
        print('deu erro')

    def listar_dados_produtor(self):
        pass
