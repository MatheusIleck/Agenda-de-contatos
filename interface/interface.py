import os

from agenda.agenda import Agenda
from contatos.contato import Contato
from interface import funcoes

agenda = Agenda()
class interface():
    def __init__(self) -> None:
        pass
    def mostrar_menu(menu):
        for i, items in enumerate(menu, 1):
            print(f'\033[1;33m{i}\033[m - \033[1;35m{items["comando_principal"]}\033[m')
        
    def mostrar_submenu(submenu):
        for i, opcao_submenu in enumerate(submenu, 1):
            print(f'\033[1;33m{i}\033[m - \033[1;35m{opcao_submenu["nome"]}\033[m')
        
    def exibir_agendas():
        import os
        caminho_do_diretorio = 'lista_de_agendas'
        arquivos = os.listdir(caminho_do_diretorio)
        funcoes.cabecalho('Agendas')
        for arquivo in arquivos:
            print(f'\033[1;35m- {arquivo}\033[m')
        funcoes.linha()
        
    def executar_comando(resposta):
        if resposta == 1:
            funcoes.linha()
            nova_agenda = str(input('Digite o nome da agenda que deseja criar: '))
            funcoes.criar_agenda(nova_agenda)
        
        elif resposta == 2:
            interface.exibir_agendas()
           

        elif resposta == 3:
            print(f'\033[;32mSaindo...\033[m')
            quit() 
        else:
            funcoes.linha()
            print(f'\033[;31mPor favor digite um valor válido.\033[m')
        
    def executar_comando_submenu(situacao_atual, resposta_submenu, menu):
        agendas = funcoes.selecionar_agendas()
        
        while situacao_atual in 'Listar Agendas existentes':
            if resposta_submenu == 1:
                selecionar_agenda = str(input('Digite o nome da agenda que deseja selecionar: ')) + '.pkl'
                
                if selecionar_agenda in agendas:
                    agenda_atual = agenda.verificar_agenda(selecionar_agenda)
                    agenda_atual
                    subsubmenu = menu[1]['sub_comandos'][0]['subsubmenu']
                    for items in subsubmenu:
                        print(items["nome"])
                    teste = int(input('Qual vc deseja: '))
                    if teste  == 1:
                        lista_contatos = Contato.criar_contatos()
                        #continuar a partir daqui
                        agenda.salvar_contatos(lista_contatos, agenda_atual)
                    
            elif resposta_submenu == 2:
                selecionar_agenda = str(input('Digite o nome da agenda que deseja editar: ')) + '.pkl'
                
                if selecionar_agenda in agendas:
                    novo_nome_agenda = str(input('Digite o novo nome da agenda: ')) + '.pkl'
                    os.rename("lista_de_agendas/" + selecionar_agenda, "lista_de_agendas/" +novo_nome_agenda)
                    break
                    
            else:
                print('Por favor digite um valor válido')
                break
                
                
                
                
                
                
            '''elif resposta == 3:
            lista_contatos = Contato.criar_contatos()
            agenda.salvar_contatos(lista_contatos)
            
        elif resposta == 4:
            esperando_por_input = False
            try:
                #exibe os contatos
                agenda.exibir_contatos()
                
                #pega a lista de contatos
                contatos = agenda.pegar_contatos()
                
                #verifica se existe items na lista
                if len(contatos) > 0:
                    esperando_por_input = True
                    
                while esperando_por_input == True:
                    funcoes.linha()
                    
                    #pergunta ao usuario qual contato ele deseja editar
                    index_contato = int(input('Qual contato você deseja editar?'))
                    
                    #recebe o contato escolhido
                    contato_escolhido = agenda.encontrar_contato(index_contato)
                    
                    #verifica se existe o usuario na lista de contatos
                    if contato_escolhido in contatos:
                        escolher_campo_edicao_contato = int(input('O que você deseja editar? (0 para editar o nome e 1 para editar o número): '))
                        if escolher_campo_edicao_contato == 0:
                            contato_escolhido["nome"] = funcoes.sanitizar_nome('Digite o Nome: ')
                            
                           
                        elif escolher_campo_edicao_contato == 1:
                            contato_escolhido["numero"] = funcoes.sanitizar_numero('Digite o Número: ')
                            
                        else:
                            print(f'\033[;31mPor favor digite um valor válido.\033[m')  
                        
                        agenda.editar_contatos(index_contato, contato_escolhido)
                        agenda.salvar_contatos()
                           
                        esperando_por_input = False
                        
            except(KeyboardInterrupt):
                print(f'\033[32mSaindo...\033[m')
        
            except(ValueError,TypeError):
                print(f'\033[;31mPor favor digite um valor válido.\033[m')
            
            except(IndexError):
                print(f'\033[;31mPor favor digite um valor válido.\033[m')
        
        elif resposta == 5:
            esperando_por_input = False
            try:
                agenda.exibir_contatos()
                contatos = agenda.pegar_contatos()
                if len(contatos) > 0:
                    esperando_por_input = True
                while esperando_por_input == True:
                    funcoes.linha()
                    index_contato = int(input('Qual contato você deseja remover?'))
                    contato_escolhido = agenda.encontrar_contato(index_contato)
                    if contato_escolhido in contatos:    
                        agenda.remover_contatos(index_contato)
                        agenda.salvar_contatos()
                        esperando_por_input = False
                        
            except (ValueError,TypeError):
                print(f'\033[;31mPor favor digite um valor válido\033[m')
            except KeyboardInterrupt:
                print(f'\033[;32mSaindo...\033[m')
            except(IndexError):
                print(f'\033[;31mPor favor digite um valor válido.\033[m')
        
        elif resposta == 6:
            agenda.exibir_contatos()'''
        
        
            
