import pickle
import re

from funcoes.funcoes import cabecalho, linha, sanitizar_nome, sanitizar_numero


class Agenda():
    def __init__(self):
        self.contatos = list()
        

    def criar_agenda(self, nova_agenda):
        try:
            import os
            #define o caminho
            caminho = 'lista_de_agendas'
            
            #verifica se o diretorio 'lista_de_agendas' não existe
            if not os.path.exists(caminho):
                
                #cria o diretorio se ele não existir
                os.makedirs(caminho)
                
            #Define o caminho aonde eu quero salvar o arquivo, juntando a pasta com o nome do arquivo que o usuario escolheu    
            caminho_do_arquivo = os.path.join(caminho, nova_agenda +'.pkl')
            
            if os.path.isfile(caminho_do_arquivo):
                print(f'\033[;31mErro: Ja existe uma agenda com esse nome!\033[m')
                pass
            
            #abre o arquivo em modo de escrita
            with open(caminho_do_arquivo, 'wb') as arquivo:
                #salva o arquivo
                pickle.dump(nova_agenda, arquivo)
                
        except OSError:
            linha()
            print(f'\033[;31mErro: Por favor digite o nome do arquivo sem caracteres especiais ou espaços!\033[m')

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
        with open("lista_de_agendas\Agenda.pkl", 'rb') as arquivo:
            lista = pickle.load(arquivo)
        if len(lista) > 0:
            for i, contato in enumerate(lista):
                print(f'\033[1;32m{i}- Nome:\033[m {contato["nome"]:<30} \033[1;32mNúmero: \033[m{contato["numero"]:>3}')
                i+= 1  
        else:
             print(f'\033[;31mVocê não tem contatos.\033[m')
             
    def editar_contatos(self, index_contato, contato_escolhido):
        self.contatos[index_contato]["nome"] = contato_escolhido["nome"]
        self.contatos[index_contato]["numero"] = contato_escolhido["numero"]
        print(f'\033[;32mContato Atualizado.\033[m')
                           
    def remover_contatos(self, remove_contato):
        self.contatos.pop(remove_contato)
        
    
    def encontrar_contato(self, numero):
        numero = self.contatos[numero]
        return numero
   
    def pegar_contatos(self):
        return self.contatos

    def teste():
        import os
        caminho_do_diretorio = 'lista_de_agendas'
        arquivos = os.listdir(caminho_do_diretorio)
        for arquivo in arquivos:
            print(arquivo)
        
