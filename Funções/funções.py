import pickle

from utilitarios.utilitarios import leia_int
from contatos.contato import Contato

def cria_contato(agenda):
    continuar = 'S'
    while continuar in 'S':
        nome = str(input('Digite o Nome: '))
        numero = int(input('Digite o numero: '))
        pessoa = Contato(nome, numero)
        agenda.adiciona_contato(pessoa)
        continuar = str(input('Deseja continuar: ')).upper()
        if continuar in 'N':
            break

def le_arquivo(self):
    with open("Agenda.pkl", 'rb') as arquivo:
        lista = pickle.load(arquivo)
    return lista
