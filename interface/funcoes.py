import pickle
import re
import os
    
def cores(indice):
    cores = {'roxo':'\033[1;35m',
             'verde':'\033[;32m',
             'vermelho':'\033[;31m',
             'amarelo':'\033[1;33m',
             'limpa':'\033[m'}
    return cores[indice]

def linha(tam=60):
    return print(cores("verde")+ '-' * tam)

def cabecalho(txt):
    linha()
    print(f'{cores("verde") + txt.center(60)}')
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
    try:
        novo_menu = menu[resposta - 1].get('sub_comandos')
        return novo_menu
    except IndexError:
        print(cores("vermelho") + 'Por favor digite um valor válido')
    
def leia_int(msg):
    while True:
        try:
            número = int(input(cores("roxo") + msg))
        except ValueError:
            print(cores("vermelho") + 'Erro, por favor digite um número válido.')
        except KeyboardInterrupt:
            print(cores("verde") + 'Saindo...')
            exit()
        else:
            return número
        
def sanitizar_nome(msg):
    
    padrao_nome = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*([ ]?[a-zA-Z0-9]+)*$")
    nome = str(input(msg))
    
    while not padrao_nome.match(nome):
        print(cores("vermelho") + 'ERRO:Dados inválidos' + cores("limpa"))
        nome = str(input(cores("verde") + 'Digite o Nome: '))
    else:
        return nome
def sanitizar_numero(msg):
    padrao_numero = re.compile(r"[0-9]{11}$")
    numero = str(input(msg))
    while not padrao_numero.match(numero):
        print(cores("vermelho") + 'ERRO:Dados invalidos' + cores("limpa"))
        numero = str(input(cores("verde") +'Digite o Número com o DDD (xxxxxxxxxxx): '))
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
                print(cores("vermelho") + 'ERRO:Ja existe uma agenda com esse nome!' + cores("limpa"))
                pass
            
            #abre o arquivo em modo de escrita
            with open(caminho_do_arquivo, 'wb') as arquivo:
                #salva o arquivo
                pickle.dump(nova_agenda, arquivo)
                
        except OSError:
            linha()
            print(cores("vermelho") + 'ERRO:Por favor digite o nome do arquivo sem caracteres especiais ou espaços!' + cores("limpa"))

def selecionar_agendas():
    caminho_do_diretorio = 'lista_de_agendas'
    arquivos = os.listdir(caminho_do_diretorio)
    return arquivos
