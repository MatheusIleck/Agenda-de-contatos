import pickle
import os
import re

from funcoes.funções import cabecalho, linha, sanitizar_nome, sanitizar_numero


class Agenda():
    def __init__(self):
        self.contatos = list()
        Agenda.criar_arquivo(self)
        Agenda.verificar_agenda(self)

    def criar_arquivo(self):
        import os
        caminho = "Agenda.pkl"
        if os.path.isfile(caminho):
            pass
        else:
            with open("Agenda.pkl", "wb") as arquivo:
                pickle.dump(self.contatos, arquivo)

    def verificar_agenda(self):
        with open("Agenda.pkl", 'rb') as arquivo:
            lista = pickle.load(arquivo)
        if len(lista) > 0:
           self.contatos = lista
           return self.contatos
        else:
            self.contatos = []
            return self.contatos

    def salvar_contatos(self, contatos=None):
        if contatos == None:
            with open("agenda.pkl", 'wb') as arquivo:
                pickle.dump(self.contatos, arquivo)
        else:
            self.contatos.extend(contatos)
            with open("agenda.pkl", 'wb') as arquivo:
                    pickle.dump(self.contatos, arquivo)

    def exibir_contatos(self):
        cabecalho('AGENDA')
        with open("Agenda.pkl", 'rb') as arquivo:
            lista = pickle.load(arquivo)
        if len(lista) > 0:
            for i, contato in enumerate(lista):
                print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                i+= 1  
        else:
             print(f'\033[;31mVocê não tem contatos.\033[m')
             
    def editar_contatos(self, contato_escolhido, nome, numero):
        self.contatos[contato_escolhido]["nome"] = nome
        self.contatos[contato_escolhido]["numero"] = numero
        print(f'\033[;32mContato Atualizado.\033[m')
                           
    def remover_contatos(self, remove_contato):
        self.contatos.pop(remove_contato)
        
    
    def encontrar_contato(self, numero):
        numero = self.contatos[numero]
        return numero
   
    def pegar_contatos(self):
        return self.contatos

