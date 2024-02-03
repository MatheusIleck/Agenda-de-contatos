import re

from agenda.agenda import Agenda
from interface.funcoes import sanitizar_nome, sanitizar_numero, cores


class Contato():
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    
    def criar_contatos():
        try:
            contatos = list()
            while True:
                #Pega os dados do novo contato e salva dentro de uma instancia
                nome = sanitizar_nome(cores("roxo") + 'Digite o nome: ')
                numero = sanitizar_numero(cores("roxo") + 'Digite o Número com o DDD: (xxxxxxxxxxx) ')
                novo_contato = Contato(nome, numero)
                
                #Pega os valores com dicionario e adiciona em uma lista
                dados = dict()
                dados = {'nome': novo_contato.nome, 'numero': novo_contato.numero}
                contatos.append(dados)
                
                
                continuar = input("Deseja adicionar outro contato? ").upper()
                while continuar not in 'SsNn':
                    continuar = str(input(cores("erro") + 'Por favor digite um digito válido: ')).upper()
                    
                if continuar in 'N' or continuar == "NAO":
                    return contatos     
        
                    

        except KeyboardInterrupt:
            print("\033[;32mSaindo...\033[m")
