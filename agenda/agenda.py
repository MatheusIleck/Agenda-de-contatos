import pickle
import os

from utilitarios.utilitarios import cabecalho
from Funções.funções import le_arquivo


class Agenda():
    def __init__(self):
        self.contatos = list()
        Agenda.cria_arquivo(self)
        Agenda.verifica_agenda(self)
    def adiciona_contato(self, Contato):
        dados = dict()
        dados = {'nome': Contato.nome, 'numero': Contato.numero}
        self.contatos.append(dados)
        self.salva_contato()

    def cria_arquivo(self):
        import os
        caminho = "Agenda.pkl"
        if os.path.isfile(caminho):
            pass
        else:
            with open("Agenda.pkl", "wb") as arquivo:
                pickle.dump(self.contatos, arquivo)

    def verifica_agenda(self):
        with open("Agenda.pkl", 'rb') as arquivo:
            lista_contatos = pickle.load(arquivo)
        if len(lista_contatos) > 0:
            self.lista_contatos = le_arquivo(self)
            self.contatos = lista_contatos
        else:
            self.contatos = []

    def salva_contato(self):
        with open("agenda.pkl", 'wb') as arquivo:
            pickle.dump(self.contatos, arquivo)

    def exibe_contato(self):
        cabecalho('AGENDA')
        if len(self.contatos) > 0:
                for i, contato in enumerate(self.contatos):
                    print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                    i+= 1

    def edita_contato(self):
        if len(self.contatos) > 0:
                for i, contato in enumerate(self.contatos):
                    print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                    i+= 1
                    edita_contato = int(input('Qual contato você deseja editar?'))
                    self.contatos[edita_contato]["nome"] = str(input('Digite o Nome: '))
                    self.contatos[edita_contato]["numero"] = str(input('Digite o numero: '))
                    Agenda.salva_contato(self)
        else:
            print(f'Você não tem contatos')

