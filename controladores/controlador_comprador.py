from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self, controlador_principal):
        self.__tela_comprador = TelaComprador(self)
        self.__compradores = []
        self.__controlador_principal = controlador_principal
        self.__tela_aberta = False

    def inclui_comprador(self, nome, cpf, nascimento, email, celular, senha):
        comprador = Comprador(nome, cpf, nascimento, email, celular, senha)
        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
                return comprador
                #fazer metodo acao realizada com sucesso
        except SystemError:
            self.__tela_comprador.usuario_ja_existe()

    def retorna_comprador_e_senha_pelo_cpf(self, cpf):
        for comprador in self.__compradores:
            if comprador.cpf == cpf:
                return [comprador, comprador.senha]

    def escolher_acao(self):
        self.__tela_aberta = True
        opcoes = {1: self.ver_meus_ingressos, 2: self.ver_eventos_disponiveis,3: self.ver_eventos_favoritos,
                  4: self.favoritar_evento, 5: self.comprar_ingresso, 6: self.alterar_dados_comprador,
                  7: self.excluir_comprador, 8: self.sair_da_conta}
        while self.__tela_aberta:
            opcao = self.__tela_comprador.mostrar_opcoes_comprador()
            opcoes[opcao]()

    def alterar_dados_comprador(self):
        dicionario_dados = {1: self.__controlador_principal.usuario_logado.nome,
                            2: self.__controlador_principal.usuario_logado.cpf,
                            3: self.__controlador_principal.usuario_logado.nascimento,
                            4: self.__controlador_principal.usuario_logado.email,
                            5: self.__controlador_principal.usuario_logado.celular,
                            6: self.__controlador_principal.usuario_logado.senha}
        self.__tela_comprador.listar_dados_comprador(self.__controlador_principal.usuario_logado)
        num_do_dado, dado_a_ser_alterado = self.__tela_comprador.escolher_dado_para_alterar()
        dicionario_dados[num_do_dado] = dado_a_ser_alterado


    def excluir_comprador(self):
        usuario_para_excluir = self.__controlador_principal.usuario_logado
        print(usuario_para_excluir)
        self.__compradores.remove(usuario_para_excluir)
        self.sair_da_conta()

    def ver_meus_ingressos(self):
        self.__tela_comprador.mostrar_meus_ingressos(self.__controlador_principal.usuario_logado.meus_ingressos)

    def ver_eventos_disponiveis(self):
        self.__controlador_principal.atualizar_eventos_disponiveis()
        self.__tela_comprador.mostrar_eventos_disponiveis(self.__controlador_principal.eventos_disponiveis)

    def ver_eventos_favoritos(self):
        self.__tela_comprador.mostrar_eventos_favoritos(self.__controlador_principal.usuario_logado.eventos_favoritos)

    def favoritar_evento(self):
        codigo_evento_para_favoritar = self.__tela_comprador.pegar_dados_para_favoritar_evento()
        for evento in self.__controlador_principal.eventos_disponiveis:
            if evento.codigo == codigo_evento_para_favoritar:
                self.__controlador_principal.usuario_logado.eventos_favoritos.append(evento)

    def transferir_ingresso(self):
        cpf_para_transferir, evento, codigo_ingresso = self.__tela_comprador.pegar_dados_transferir_ingresso()
        for ingresso in self.__controlador_principal.usuario_logado.meus_ingressos:
            if ingresso.evento == evento and ingresso.codigo == codigo_ingresso:
                ingresso_para_transferir = ingresso
                self.__controlador_principal.usuario_logado.meus_ingressos.remove(ingresso_para_transferir)
                comprador_para_transferir = self.retorna_comprador_e_senha_pelo_cpf(cpf_para_transferir)[0]
                comprador_para_transferir.meus_ingressos.append(ingresso_para_transferir)

    def sair_da_conta(self):
        self.__tela_aberta = False
        self.__controlador_principal.deslogar()

    def comprar_ingresso(self):
        self.ver_eventos_disponiveis()
        nome_evento = self.__tela_comprador.pegar_evento_para_compra()
        ingresso = None
        for evento in self.__controlador_principal.eventos_disponiveis:
            if nome_evento == evento.nome:
                ingresso = evento.ingressos[0]
                evento.ingressos.remove(ingresso)
                evento.ingressos_vendidos.append(ingresso)
                self.__controlador_principal.usuario_logado.meus_ingressos.append(ingresso)
        return ingresso