import pickle
import re

from interface.funcoes import cabecalho, linha, sanitizar_nome, sanitizar_numero, cores


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

        else:
            with open(caminho + agenda_selecionada, 'wb') as arquivo:
                    pickle.dump(self.contatos, arquivo)

    def exibir_contatos(self, agenda_atual):
        caminho = "lista_de_agendas/"
        cabecalho('AGENDA')
        with open(caminho + agenda_atual , 'rb') as arquivo:
            lista = pickle.load(arquivo)
        
        if isinstance(lista, list) and len(lista) > 0:
            for i, contato in enumerate(lista):
                print(f'{cores("amarelo")}{i} - Nome: {cores("verde") + contato["nome"]:<30} {cores("amarelo")}Número: {cores("verde") + contato["numero"]:>3}')
                i+= 1  
        else:
             print(cores("vermelho") + 'Você não tem contatos.')
             
    def editar_contatos(self, index_contato, contato_escolhido, contatos):
        contatos[index_contato]["nome"] = contato_escolhido["nome"]
        contatos[index_contato]["numero"] = contato_escolhido["numero"]
        self.contatos = contatos
        print(cores("verde") + 'Contato Atualizado.')
        
        return self.contatos
                           
    def remover_contatos(self, contatos_existentes, index_contato):
        contatos_existentes.pop(index_contato)
        self.contatos = contatos_existentes
        return self.contatos
            
    def pegar_contatos(self, agenda_atual):
         with open("lista_de_agendas/" + agenda_atual , 'rb') as arquivo:
            lista = pickle.load(arquivo)
            return lista

        
