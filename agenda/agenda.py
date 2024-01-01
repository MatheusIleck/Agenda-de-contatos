import pickle
from utilitarios.utilitarios import cabecalho
class Agenda():
    def __init__(self):
        self.contatos = list()

    def adicionarContato(self, Contato):
        dados = dict()
        dados = {'nome': Contato.nome, 'numero': Contato.numero}
        self.contatos.append(dados)
        self.salvarContatos()
    def criaArquivo(self):
        import os
        caminho = "Agenda.pkl"
        if os.path.isfile(caminho):
            pass
        else:
            with open("Agenda.pkl", "wb") as arquivo:
                pickle.dump(self.contatos, arquivo)

    def salvarContatos(self):
        with open("Agenda.pkl", 'wb') as arquivo:
            pickle.dump(self.contatos, arquivo)

    def exibeContato(self):
        cabecalho('AGENDA')
        with open("Agenda.pkl", 'rb') as arquivo:
            lista_contatos = pickle.load(arquivo)
        for i, contato in enumerate(lista_contatos):
            print(f'\033[1;32m{i+1}º Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
            i+= 1