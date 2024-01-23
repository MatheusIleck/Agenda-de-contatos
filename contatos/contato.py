import re

from agenda.agenda import Agenda
from interface.funcoes import sanitizar_nome
from interface.funcoes import sanitizar_numero


class Contato():
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    
    def criar_contatos():
        try:
            contatos = list()
            while True:
                #Pega os dados do novo contato e salva dentro de uma instancia
                nome = sanitizar_nome('Digite o nome: ')
                numero = sanitizar_numero('Digite o Numero: ')
                novo_contato = Contato(nome, numero)
                
                #Pega os valores com dicionario e adiciona em uma lista
                dados = dict()
                dados = {'nome': novo_contato.nome, 'numero': novo_contato.numero}
                contatos.append(dados)
                
                
                continuar = input("Deseja adicionar outro contato? ").upper()
                while continuar not in 'SsNn':
                    continuar = str(input('Por favor digite um valor válido: ')).upper()
                    
                if continuar in 'N':
                    return contatos
                    break
                    
        
                    

        except KeyboardInterrupt:
            print("\033[;32mSaindo...\033[m")
