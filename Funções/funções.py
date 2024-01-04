import pickle

from utilitarios.utilitarios import leia_int
from contatos.contato import Contato

def cria_contato(agenda):
    try:
        continuar = 'S'

        while continuar in 'S':
            nome = str(input('Digite o Nome: '))
            numero = int(input('Digite o numero: '))
            while len(str(numero)) > 11 or len(str(numero)) < 11:
                numero = int(input('Por favor digite um numero valido: '))
            pessoa = Contato(nome, numero)
            agenda.adiciona_contato(pessoa)
            continuar = str(input('Deseja continuar: ')).upper()
            if continuar in 'N':
                break
    except KeyboardInterrupt:
        print("\033[;32mSaindo...\033[m")
        quit()
def le_arquivo(self):
    with open("Agenda.pkl", 'rb') as arquivo:
        lista = pickle.load(arquivo)
    return lista
