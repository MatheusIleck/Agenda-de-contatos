import pickle
import os
import re

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
        else:
            print('Você não tem contatos')

    def edita_contato(self):
        padrao_nome = re.compile(r"^[A-Za-z]+(?:[^\S\r\n]+[A-Za-z]+)*$")
        padrao_numero = re.compile(r"[0-9]{11}")
        if len(self.contatos) > 0:
                for i, contato in enumerate(self.contatos):
                    print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                    i+= 1
                edita_contato = int(input('Qual contato você deseja editar?'))
                while True:
                    if edita_contato > len(self.contatos) - 1:
                        print(f'Por favor Digite um valor valido')
                    else:
                        self.contatos[edita_contato]["nome"] = str(input('Digite o Nome: '))
                        self.contatos[edita_contato]["numero"] = str(input('Digite o numero: '))
                        if padrao_nome.match(self.contatos[edita_contato]["nome"]) and padrao_numero.match(self.contatos[edita_contato]["numero"]):
                            Agenda.salva_contato(self)
                            break
                        else:
                            print('Por favor digite valores validos')
        else:
            print(f'Você não tem contatos')

    def remove_contato(self):

        if len(self.contatos) > 0:
            for i, contato in enumerate(self.contatos):
                print(
                    f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                i += 1
            remove_contato = int(input('Qual contato você deseja remover?'))
            self.contatos.pop(remove_contato)
            Agenda.salva_contato(self)
        else:
            print(f'Você não tem contatos')
