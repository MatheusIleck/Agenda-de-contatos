from interface.interface import interface
from interface.funcoes import leia_int, selecionar_submenu, menu


nova_interface = interface
menu = menu()
while True:
   nova_interface.mostrar_menu(menu)
   resposta = leia_int('Digite a opção: ')
   nova_interface.executar_comando(resposta)
   #pega o submenu pela chave atraves do get
   submenu = selecionar_submenu(resposta, menu)
   if submenu: 
      situacao_atual = menu[resposta - 1]['comando_principal'] 
      nova_interface.mostrar_submenu(submenu)
      resposta_submenu = leia_int('Digite a opção: ')
      nova_interface.executar_comando_submenu(situacao_atual, resposta_submenu, menu)
      
         
      
