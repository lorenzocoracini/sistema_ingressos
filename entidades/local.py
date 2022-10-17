class Local:
    def __init__(self, rua:str, bairro:str, cidade:str, cep:str, lotacao_maxima:int, aluguel:float):
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep
        self.__lotacao_maxima = lotacao_maxima
        self.__aluguel = aluguel

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, nova_rua):
        self.__rua = nova_rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self,novo_bairro):
        self.__bairro = novo_bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self,nova_cidade):
        self.__cidade = nova_cidade

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self,novo_cpf):
        self.__cep = novo_cpf

    @property
    def lotacao_maxima (self):
        return self.__lotacao_maxima

    @lotacao_maxima.setter
    def lotacao_maxima(self,nova_lotacao_maxima):
        self.__lotacao_maxima = nova_lotacao_maxima

    @property
    def aluguel(self):
        return self.__aluguel

    @aluguel.setter
    def aluguel(self, novo_aluguel):
        self.__aluguel = novo_aluguel

