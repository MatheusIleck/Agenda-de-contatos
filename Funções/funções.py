import pickle
import re
    

def linha(tam=60):
    return print('-' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(60))
    linha()

def menu(lista):
    cabecalho('Menu')
    c = 1
    for items in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;35m{items}\033[m')
        c += 1
    linha()
    
def leia_int(msg):
    while True:
        try:
            número = int(input(msg))
        except ValueError:
            print('\033[0;31mErro, por favor digite um número Valido. \033[m')
        except KeyboardInterrupt:
            print("\033[;32mSaindo...\033[m")
            exit()
        else:
            return número
        
def sanitizar_nome(msg):
    padrao_nome = re.compile(r"^[A-Za-z]+(?:[^\S\r\n]+[A-Za-z]+)*$")
    nome = str(input(msg))
    
    while not padrao_nome.match(nome):
        print('\033[;31mERRO: Dados invalidos\033[m')
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
         
     