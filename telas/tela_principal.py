class TelaPrincipal:

    def mostra_tela_principal(self):
        print('*' * 20)
        print('ESCOLHA SUA CATEGORIA')
        print('1 - COMPRADOR')
        print('2 - PRODUTOR')
        print('0 - SAIR')
        opcao = int(input('ESCOLHA A OPÇÃO: '))

        return opcao
