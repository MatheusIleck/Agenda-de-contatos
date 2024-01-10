import pickle
import re

from utilitarios.utilitarios import leia_int
from contatos.contato import Contato


def cria_contato(agenda):
    padrao_nome = re.compile(r"^[A-Za-z]+(?:[^\S\r\n]+[A-Za-z]+)*$")
    padrao_numero = re.compile(r"[0-9]{11}")
    continuar = 'S'
    try:
        while True:
            if continuar in 'S':
                nome = str(input('Digite o Nome: '))
                numero = str(input('Digite o Numero: '))
                if padrao_nome.match(nome) and padrao_numero.match(numero):
                    pessoa = Contato(nome, numero)
                    agenda.adiciona_contato(pessoa)
                else:
                    print('Por favor digite os dados corretamente')
            continuar = str(input('Deseja continuar: ')).upper()
            if continuar == 'N':
                break
            else:
                print('Por favor digite um valor valido')

    except KeyboardInterrupt:
        print("\033[;32mSaindo...\033[m")
def le_arquivo(self):
    with open("Agenda.pkl", 'rb') as arquivo:
        lista = pickle.load(arquivo)
    return lista
