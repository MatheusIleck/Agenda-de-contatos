import os
import glob

from agenda.agenda import Agenda
from contatos.contato import Contato
from interface.funcoes import leia_int, selecionar_submenu, menu,cabecalho, linha, criar_agenda, selecionar_agendas, sanitizar_nome, sanitizar_numero, cores

agenda = Agenda()
class Interface():
    def __init__(self) -> None:
        pass
    def mostrar_menu(menu):
        for i, items in enumerate(menu, 1):
            print(f'\033[1;33m{i} - \033[1;35m{items["comando_principal"]}')
        
    def mostrar_submenu(submenu):
        for i, opcao_submenu in enumerate(submenu, 1):
            print(f'\033[1;33m{i} - \033[1;35m{opcao_submenu["nome"]}')
        
    def exibir_agendas():
        import os
        caminho_do_diretorio = 'lista_de_agendas'
        arquivos = os.listdir(caminho_do_diretorio)
        cabecalho('Agendas')
        for arquivo in arquivos:
            print(cores("amarelo") +'- '+ arquivo)
        linha()
        
    def executar_comando(resposta):
        if resposta == 1:
            linha()
            nova_agenda = str(input('Digite o nome da agenda que deseja criar: ')) + '.pkl'
            criar_agenda(nova_agenda)
            agenda.salvar_contatos(nova_agenda)
            nova_agenda = agenda.verificar_agenda(nova_agenda)
            return nova_agenda
            
        
        elif resposta == 2:
            lista_de_agenda = glob.glob("./lista_de_agendas/*.pkl")
            if lista_de_agenda:
                Interface.exibir_agendas()
                return 'agendas listadas'
            else:
                print(cores("vermelho") + 'ERRO:Você não tem agendas.')
                return 'sem agendas'

        elif resposta == 3:
            print(f'\033[;32mSaindo...')
            quit() 
        else:
            linha()
            print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.')
        
    def executar_comando_submenu(situacao_atual, resposta_submenu, agenda_selecionada, entrar_na_agenda):
        try:
            #pega o diretorio das agendas
            diretorio_agendas = selecionar_agendas()
            #enquanto situação atual estiver em "listar agendas existentes"
            while entrar_na_agenda:
                
                #Se a resposta do usuario é igual a 1
                if resposta_submenu == 1:
                
                    #pede o nome da agenda ao usuario  
                    selecionar_agenda = str(input('Digite o nome da agenda que deseja selecionar: ')) + '.pkl'   
                    
                    #verifica se existe uma agenda com esse nome dentro do diretorio de agendas 
                    if selecionar_agenda in diretorio_agendas:
                        situacao_atual = 'agenda selecionada'
                        return selecionar_agenda
                        
                elif resposta_submenu == 2:
                    linha()
                    selecionar_agenda = str(input('Digite o nome da agenda que deseja editar: ')) + '.pkl'
                    
                    if selecionar_agenda in diretorio_agendas:
                        novo_nome_agenda = str(input('Digite o novo nome da agenda: ')) + '.pkl'
                        os.rename("lista_de_agendas/" + selecionar_agenda, "lista_de_agendas/" +novo_nome_agenda)  
                        linha()
                        
                        agenda_selecionada = False
                        return 'agenda não selecionada'
                        
                elif resposta_submenu == 3:
                    
                    caminho_do_diretorio = 'lista_de_agendas/'
                    lista_de_agenda = glob.glob("./lista_de_agendas/*.pkl")
                
                    if lista_de_agenda:
                        try:
                            selecionar_agenda = str(input('Digite o nome da agenda que deseja remover: ')) + '.pkl'
                            os.unlink(caminho_do_diretorio + selecionar_agenda)
                            print(f'\033[0;32mAgenda removida!')
                            return ''
                        except FileNotFoundError:
                            print('Essa agenda não existe.')
                        
                    else:
                        linha()
                        print('\033[0;31mNão existem agendas ')
                        
                    return ''
                
                elif resposta_submenu == 4:
                    return 'agenda não selecionada'
                else:
                    return 'Por favor digite um valor valido'
        except (IndexError):
            print('Por favor digite um valor válido')
            
        while agenda_selecionada:   
            try:
                if resposta_submenu == 1:
                    linha()
                    lista_contatos = Contato.criar_contatos()
                    linha()
                    contatos_existentes = agenda.verificar_agenda(agenda_selecionada)
                    contatos_existentes.extend(lista_contatos)
                    agenda.salvar_contatos(agenda_selecionada, contatos_existentes)
                    return agenda_selecionada

            
                elif resposta_submenu == 2: 
                    #exibe os contatos                    
                    agenda.exibir_contatos(agenda_selecionada)
                    
                    #pega a lista de contatos
                    contatos = agenda.pegar_contatos(agenda_selecionada)
                    
                    #verifica se existe items na lista
                    
                    if  len(contatos) > 0:
                        linha()
                        
                        #pergunta ao usuario qual contato ele deseja editar
                        index_contato = int(input('Qual contato você deseja editar?'))
                        
                        #recebe o contato escolhido
                        contato_escolhido = contatos[index_contato]
                    
                        #verifica se existe o usuario na lista de contatos
                        if contato_escolhido in contatos:
                            escolher_campo_edicao_contato = int(input('O que você deseja editar? (0 para editar o nome e 1 para editar o número): '))
                            if escolher_campo_edicao_contato == 0:
                                contato_escolhido["nome"] = sanitizar_nome('Digite o Nome: ')
                                    
                                
                            elif escolher_campo_edicao_contato == 1:
                                contato_escolhido["numero"] = sanitizar_numero('Digite o Número: ')
                                    
                            else:
                                print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.')  
                                
                            contatos_atualizados = agenda.editar_contatos(index_contato, contato_escolhido, contatos)
                            agenda.salvar_contatos(agenda_selecionada, contatos_atualizados)
                            return agenda_selecionada
                    else:
                        print('você não tem contatos')
                        break
                    
                elif resposta_submenu == 3:
                    contatos = agenda.verificar_agenda(agenda_selecionada)
                    if len(contatos) > 0:
                        agenda.exibir_contatos(agenda_selecionada)
                        index_contato = leia_int('Digite o índex do contato que deseja remover: ')
                        contatos_atualizados = agenda.remover_contatos(contatos,index_contato)
                        agenda.salvar_contatos(agenda_selecionada)
                        return agenda_selecionada
                        break
                    else:
                        print(cores("vermelho") + 'ERRO:você não tem contatos')
                        break
                elif resposta_submenu == 4:
                    agenda.exibir_contatos(agenda_selecionada)
                    return agenda_selecionada
                    break
                    
                elif resposta_submenu == 5:
                    agenda_selecionada = ''
                    return agenda_selecionada
                    break
                else:
                    print(cores("vermelho") + 'ERRO:Por favor digite um valor válido!')
                    break
            except(KeyboardInterrupt):
                print(cores("verde") + 'Saindo...')
        
            
     
        
    '''elif resposta == 4:
                esperando_por_input = False
                try:
                    agenda.exibir_contatos()
                    contatos = agenda.pegar_contatos()
                    if len(contatos) > 0:
                        esperando_por_input = True
                    while esperando_por_input == True:
                        linha()
                        index_contato = int(input('Qual contato você deseja remover?'))
                        contato_escolhido = agenda.encontrar_contato(index_contato)
                        if contato_escolhido in contatos:    
                            agenda.remover_contatos(index_contato)
                            agenda.salvar_contatos()
                            esperando_por_input = False
                            
                except (ValueError,TypeError):
                    print(cores("vermelho") + 'ERRO:Por favor digite um valor válido')
                except KeyboardInterrupt:
                    print(f'\033[;32mSaindo...')
                except(IndexError):
                    print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.')
            
            elif resposta == 6:
                agenda.exibir_contatos()'''
        
        
            
