import pickle
import re

from interface.funcoes import cabecalho, linha, sanitizar_nome, sanitizar_numero


class Agenda():
    def __init__(self):
        self.contatos = list()
        

    def verificar_agenda(self, agenda):
        caminho = 'lista_de_agendas/'
        with open(caminho + agenda, 'rb') as arquivo:
            lista = pickle.load(arquivo)
        if isinstance(lista, list):
            if len(lista) > 0:
                self.contatos = lista
                return self.contatos
            else:
                self.contatos.extend(lista)
                return self.contatos
        else:
            agenda = self.contatos
            return self.contatos

    def salvar_contatos(self, agenda_selecionada, contatos=None,):
        caminho = 'lista_de_agendas/'
        if contatos == None:
            with open(caminho + agenda_selecionada, 'wb') as arquivo:
                pickle.dump(self.contatos, arquivo)

                print(f'self contatos: {self.contatos}' )
        else:
            with open(caminho + agenda_selecionada, 'wb') as arquivo:
                    pickle.dump(self.contatos, arquivo)

    def exibir_contatos(self, agenda_atual):
        caminho = "lista_de_agendas/"
        cabecalho('AGENDA')
        with open(caminho + agenda_atual , 'rb') as arquivo:
            lista = pickle.load(arquivo)
        print(lista)
        '''if len(lista) > 0:
            for i, contato in enumerate(lista):
                print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNúmero: \033[m{contato["numero"]:>3}')
                i+= 1  
        else:
             print(f'\033[;31mVocê não tem contatos.\033[m')'''
             
    def editar_contatos(self, index_contato, contato_escolhido, contatos):
        contatos[index_contato]["nome"] = contato_escolhido["nome"]
        contatos[index_contato]["numero"] = contato_escolhido["numero"]
        self.contatos = contatos
        print(f'\033[;32mContato Atualizado.\033[m')
        
        return self.contatos
                           
    def remover_contatos(self, remove_contato):
        self.contatos.pop(remove_contato)
        
    def pegar_contatos(self, agenda_atual):
         with open("lista_de_agendas/" + agenda_atual , 'rb') as arquivo:
            lista = pickle.load(arquivo)
            return lista

        
