from interface.interface import Interface
from funcoes.funções import leia_int
from comandos import comandos

interface = Interface(comandos(), "#fff")

while True:
   nova_interface.mostrar_comandos()
   resposta = leia_int('Digite a opção: ')
   nova_interface.executar_comando(resposta)

