from entidades.produtor import Produtor
from entidades.evento import Evento
from entidades.local import Local
from telas.tela_produtor import TelaProdutor
from telas.tela_evento import TelaEvento
from entidades.ingresso import Ingresso
from telas.tela_ingresso import TelaIngresso
import datetime


class ControladorProdutor:
    def __init__(self, controlador_principal):
        self.__eventos = []
        self.__produtores = []
        self.__tela_produtor = TelaProdutor(self)
        self.__tela_evento = TelaEvento(self)
        self.__tela_aberta = False
        self.__controlador_principal = controlador_principal
        self.__tela_ingresso = TelaIngresso()

    def listar_eventos(self):
        self.__tela_produtor.mostar_eventos(self.__eventos)

    def editar_evento(self):
        codigo_evento, dados_atualizados = self.__tela_produtor.alterar_evento()
        evento_a_ser_alterado = None
        for evento in self.__eventos:
            if evento.codigo == codigo_evento:
                evento_a_ser_alterado = evento
        if evento_a_ser_alterado:
            evento_a_ser_alterado.codigo = (dados_atualizados['codigo_evento'])
            evento_a_ser_alterado.data = (dados_atualizados['data_evento'])
            evento_a_ser_alterado.nome = (dados_atualizados['nome_evento'])
            evento_a_ser_alterado.descricao = (dados_atualizados['descricao_evento'])
            evento_a_ser_alterado.atracao = (dados_atualizados['atracao_evento'])
        else:
            self.__tela_produtor.evento_nao_existe()



    def inclui_produtor(self, nome, cpf, email, celular, senha):
        produtor = Produtor(nome, cpf, email, celular, senha)
        try:
            for i in self.__produtores:
                if produtor.cpf == i.cpf:
                    raise SystemError
            else:
                self.__produtores.append(produtor)
                print(self.__produtores)
                return produtor
        except SystemError:
            self.__tela_produtor.usuario_ja_existe()

    def retorna_produtor_e_senha_pelo_cpf(self, cpf):
        for produtor in self.__produtores:
            if produtor.cpf == cpf:
                return [produtor, produtor.senha]

    def escolher_acao(self):
        self.__tela_aberta = True
        opcoes = {1: self.adicionar_evento, 2: self.listar_eventos, 3: self.editar_evento,
                  4: self.remover_evento, 5: self.mostrar_historico_eventos,
                  6: self.exclui_produtor, 7: self.sair_da_conta}
        while self.__tela_aberta:
            opcao = self.__tela_produtor.mostrar_opcoes_produtor()
            opcoes[opcao]()

    def retorna_evento_pelo_codigo(self, codigo):
        for evento in self.__eventos:
            if evento.codigo == codigo:
                return evento

    def exclui_produtor(self):
        usuario_para_excluir = self.__controlador_principal.usuario_logado
        self.__produtores.remove(usuario_para_excluir)
        self.sair_da_conta()

    def listar_produtores(self):
        return self.__produtores

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pegar_dados()
        local = Local(dados_evento['rua_evento'], dados_evento['cep_evento'],
                      dados_evento['lotacao_maxima_evento'])

        evento = Evento(dados_evento['codigo_evento'], dados_evento['data_evento'], dados_evento['nome_evento'],
                        dados_evento['descricao_evento'], dados_evento['atracao_evento'],
                        local)
        lotacao = dados_evento['lotacao_maxima_evento']
        self.gerar_ingressos(lotacao, evento)
        self.incluir_no_historico_eventos(evento.nome, evento.data)

        if not self.retorna_evento_pelo_codigo(evento.codigo):
            self.__eventos.append(evento)
        else:
            self.__tela_evento.evento_ja_existe()


    def remover_evento(self):
        codigo = self.__tela_produtor.remover_evento()
        for evento in self.__eventos:
            if evento.codigo == codigo:
                self.__eventos.remove(evento)
            else:
                self.__tela_produtor.evento_nao_existe()

    def gerar_ingressos(self, lotacao, evento):
        dados = self.__tela_ingresso.pegar_dados()
        valor = dados['valor_do_ingresso']
        nome_evento = evento.nome
        lotacao = lotacao
        quantidade_de_ingressos = 0

        while quantidade_de_ingressos < lotacao:
            ingresso_novo = Ingresso(valor, quantidade_de_ingressos, nome_evento)
            quantidade_de_ingressos += 1
            evento.ingressos.append(ingresso_novo)

    def incluir_no_historico_eventos(self, nome, data):
        nome = nome
        data = data
        self.__controlador_principal.usuario_logado.historico_eventos.append({nome: data})

    def sair_da_conta(self):
        self.__tela_aberta = False
        self.__controlador_principal.deslogar()

    @property
    def eventos(self):
        return self.__eventos

    @property
    def produtores(self):
        return self.__produtores

    def mostrar_historico_eventos(self):
        self.__tela_produtor.mostar_historico_de_eventos(self.__controlador_principal.usuario_logado.historico_eventos)

    def verifica_data(self, dia, mes, ano, hora):
        hora_formatada = hora.split(":")
        esta_certa = True
        try:
            datetime.datetime(int(ano), int(mes), int(dia), int(hora_formatada[0]), int(hora_formatada[1]))
        except ValueError:
            esta_certa = False
        except IndexError:
            esta_certa = False
        return esta_certa

