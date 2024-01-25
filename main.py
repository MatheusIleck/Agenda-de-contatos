from interface.interface import Interface
from interface.funcoes import leia_int, selecionar_submenu, menu,  cabecalho


nova_interface = Interface
menu = menu()
while True:
   #mostra o menu principal
   nova_interface.mostrar_menu(menu)
   #resposta do usuario no menu principal
   resposta = leia_int('Digite a opção: ')
   nova_interface.executar_comando(resposta)
   #pega o submenu pela chave atraves do get
   submenu = selecionar_submenu(resposta, menu)
   if submenu:
      agenda_selecionada = ''
      situacao_atual = menu[resposta - 1]['comando_principal']
      nova_interface.mostrar_submenu(submenu)
      resposta_submenu = leia_int('Digite a opção: ')
      agenda_selecionada = nova_interface.executar_comando_submenu(situacao_atual, resposta_submenu, agenda_selecionada)
      novo_submenu = selecionar_submenu(resposta_submenu, submenu)
      while agenda_selecionada.endswith(".pkl"):
         cabecalho('Agenda selecionada')
         
         nova_interface.mostrar_submenu(novo_submenu)
         resposta_submenu = leia_int('Digite a opção: ')
         nova_interface.executar_comando_submenu(agenda_selecionada, resposta_submenu, situacao_atual)
         
    
   
         
      
