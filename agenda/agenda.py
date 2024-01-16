import pickle
import os
import re

from funções.funções import cabecalho, linha, sanitizar_nome, sanitizar_numero


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
            
            
    def editar_contatos(self):
            try:
                if len(self.contatos) <= 0:
                    pass
                else:
                    linha()
                    edita_contato = int(input('Qual contato você deseja editar?'))
                    while True:
                        if edita_contato > len(self.contatos) - 1:
                            edita_contato = int(input(f'\033[;31mPor favor Digite um valor valido: \033[m'))
                        else:
                            nome = sanitizar_nome('Digite o Nome: ')
                            numero = sanitizar_numero('Digite o Número: ')
                            self.contatos[edita_contato]["nome"] = nome
                            self.contatos[edita_contato]["numero"] = numero
                            print(f'\033[;32mContato Atualizado\033[m')
                            break
                       
            except (ValueError):
                print(f'\033[;31mO usuario digitou um valor invalido\033[m')
            except KeyboardInterrupt:
                print(f'\033[;32mSaindo...\033[m')

    def remover_contatos(self):
        if len(self.contatos) <= 0:
                    pass
        else:
            linha()
            remove_contato = int(input('Qual contato você deseja remover?'))
            linha()
            while True:
                if remove_contato > len(self.contatos) - 1:
                    remove_contato = int(input(f'\033[;31mPor favor Digite um valor valido: \033[m'))
                else:
                    print(f'\033[;32mContato removido!\033[m')
                    self.contatos.pop(remove_contato)
                    break
   
