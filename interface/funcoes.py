import pickle
import re
import os
    
def cores(indice):
    cores = {'primaria':'\033[1;35m',
             'secundaria':'\033[;32m',
             'terciario':'\033[;31m',
             'quaternario':'\033[1;33m',
             'limpa':'\033[m'}
    return cores[indice]

def linha(tam=60):
    return print(cores("secundaria")+ '-' * tam)

def cabecalho(txt):
    linha()
    print(f'{cores("secundaria") + txt.center(60)}')
    linha()

def menu():
    menu = [
    {'comando_principal': 'Criar Agenda'},
    {'comando_principal': 'Listar Agendas existentes',
     'sub_comandos': [
         {"nome": "Selecionar Agenda",
          'sub_comandos': [
              {'nome': 'Adicionar Contato'},
              {'nome': 'Editar Contato'},
              {'nome': 'Remover Contato'},
              {'nome': 'Exibir Contatos'},
              {'nome': 'Voltar'}
          ]},
         {"nome": "Editar Agenda"},
         {"nome": "Deletar Agenda"},
         {"nome": "Voltar"}
     ]},
    {'comando_principal': 'Sair'}
]

    return menu

def selecionar_submenu(resposta, menu):
    novo_menu = menu[resposta - 1].get('sub_comandos')
    return novo_menu
    
def leia_int(msg):
    while True:
        try:
            número = int(input(cores("primaria") + msg))
        except ValueError:
            print('\033[0;31mErro, por favor digite um número válido. \033[m')
        except KeyboardInterrupt:
            print("\033[;32mSaindo...\033[m")
            exit()
        else:
            return número
        
def sanitizar_nome(msg):
    
    padrao_nome = re.compile(r"^[A-Za-z]+(?:[^\S\r\n]+[A-Za-z]+)*$")
    nome = str(input(msg))
    
    while not padrao_nome.match(nome):
        print('\033[;31mERRO: Dados inválidos\033[m')
        nome = str(input('Digite o Nome: '))
    else:
        return nome
def sanitizar_numero(msg):
    padrao_numero = re.compile(r"[0-9]{11}$")
    numero = str(input(msg))
    while not padrao_numero.match(numero):
        print('\033[;31mERRO: Dados invalidos\033[m')
        numero = str(input('Digite o Número: '))
    else:
        return numero
         
def criar_agenda(nova_agenda):
        try:
            import os
            #define o caminho
            caminho = 'lista_de_agendas/'
            
            #verifica se o diretorio 'lista_de_agendas' não existe
            if not os.path.exists(caminho):
                
                #cria o diretorio se ele não existir
                os.makedirs(caminho)
                
            #Define o caminho aonde eu quero salvar o arquivo, juntando a pasta com o nome do arquivo que o usuario escolheu    
            caminho_do_arquivo = os.path.join(caminho, nova_agenda)
            
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

def selecionar_agendas():
    caminho_do_diretorio = 'lista_de_agendas'
    arquivos = os.listdir(caminho_do_diretorio)
    return arquivos
