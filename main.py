
from interface.interface import interface
from funções.funções import leia_int


nova_interface = interface

while True:
   nova_interface.mostrar_comandos()
   resposta = leia_int('Digite a opção: ')
   nova_interface.executar_comando(resposta)
