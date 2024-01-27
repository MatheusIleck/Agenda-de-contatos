from interface.interface import Interface
from interface.funcoes import leia_int, selecionar_submenu, menu,cabecalho, linha


nova_interface = Interface
menu = menu()
while True:
   #mostra o menu principal
   nova_interface.mostrar_menu(menu)
   #resposta do usuario no menu principal
   resposta = leia_int(f'\033[1;35mDigite a opção: \033[m')
   
   #executa o comando da interface
   acao_interface = nova_interface.executar_comando(resposta)
   
   #pega o submenu pela chave atraves do get
   submenu = selecionar_submenu(resposta, menu)
   
   #se existir um submenu:
   while acao_interface == 'agendas listadas' and submenu:
      #pega o nome do submenu
      situacao_atual = menu[resposta - 1]['comando_principal']
                         

      
      #exibe o submenu
      nova_interface.mostrar_submenu(submenu)
      entrar_na_agenda = True
      
      #recebe o valor do usuario
      agenda_selecionada = ''
      resposta_submenu = leia_int(f'\033[1;35mDigite a opção: \033[m')
      
      agenda_selecionada = nova_interface.executar_comando_submenu(situacao_atual, resposta_submenu, agenda_selecionada, entrar_na_agenda)
      novo_submenu = selecionar_submenu(resposta_submenu, submenu)
      
      nova_interface.exibir_agendas()
      while agenda_selecionada.endswith(".pkl"):
         entrar_na_agenda = False
         cabecalho('Agenda selecionada')
         
         nova_interface.mostrar_submenu(novo_submenu)
         resposta_submenu = leia_int('Digite a opção: ')
         nova_interface.executar_comando_submenu(situacao_atual, resposta_submenu, agenda_selecionada, entrar_na_agenda)
      
    
   
         
      
