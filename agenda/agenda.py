import pickle
import os
import re

from funções.funções import cabecalho


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
        else:
            self.contatos = []

    def salvar_contatos(self, contatos):
        self.contatos.extend(contatos)
        with open("agenda.pkl", 'wb') as arquivo:
            pickle.dump(self.contatos, arquivo)

    def exibir_contatos(self):
        cabecalho('AGENDA')
        with open("Agenda.pkl", 'rb') as arquivo:
            lista = pickle.load(arquivo)
        if len(lista)>0:
            for i in range(len(lista)):
                print(f'O nome é {lista[i]["nome"]}')
        else:
            print('Você não tem contatos')
            
    def editar_contatos(self):
        if len(self.contatos) > 0:
                for i, contato in enumerate(self.contatos):
                    print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                    i+= 1
                try:
                    edita_contato = int(input('Qual contato você deseja editar?'))
                    while True:
                        if edita_contato > len(self.contatos) - 1:
                            edita_contato = int(input(f'\033[;31mPor favor Digite um valor valido: \033[m'))
                        else:
                            nome = str(input('Digite o nome: '))
                            numero = str(input('Digite o numero: '))
                            Agenda.salvar_contatos(self)
                            break
                except (ValueError):
                    print(f'\033[;31mO usuario digitou um valor invalido\033[m')
                except KeyboardInterrupt:
                    print(f'\033[;32mSaindo...\033[m')
        else:
            print(f'Você não tem contatos')

    def remover_contatos(self):

        if len(self.contatos) > 0:
            for i, contato in enumerate(self.contatos):
                print(
                    f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNumero: \033[m{contato["numero"]:>3}')
                i += 1
            try:
                remove_contato = int(input('Qual contato você deseja remover?'))
                while True:
                    if remove_contato > len(self.contatos) - 1:
                        remove_contato = int(input(f'\033[;31mPor favor Digite um valor valido: \033[m'))
                    else:
                        self.contatos.pop(remove_contato)
                        Agenda.salvar_contato(self)
                        break
            except (ValueError):
                print(f'\033[;31mPor favor digite um valor valido\033[m')
            except KeyboardInterrupt:
                print(f'\033[;32mSaindo...\033[m')
        else:
            print(f'Você não tem contatos')
