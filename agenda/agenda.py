import pickle


from utilitarios.utilitarios import cabecalho
from Funções.funções import le_arquivo


class Agenda():
    def __init__(self):
        self.contatos = list()
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
        print(self.contatos)

    def exibe_contato(self):
        cabecalho('AGENDA')
        with open("Agenda.pkl", 'rb') as arquivo:
            lista_contatos = pickle.load(arquivo)
        if len(lista_contatos) > 0:
            for i, contato in enumerate(lista_contatos):
                print(f'\033[1;32m{i+1}º Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                i+= 1
        else:
            print(f'Você não tem contatos')