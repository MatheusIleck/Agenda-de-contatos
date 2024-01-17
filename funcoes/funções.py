import re
        
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
         
     