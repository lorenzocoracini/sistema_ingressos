from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, nascimento: str, email: str, celular: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__email = email
        self.__celular = celular

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular
