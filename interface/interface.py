import os
import glob

from agenda.agenda import Agenda
from contatos.contato import Contato
from interface.funcoes import leia_int, cabecalho, linha, criar_agenda, selecionar_agendas, sanitizar_nome, sanitizar_numero, cores

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
            nova_agenda = str(input('Digite o nome da agenda que deseja criar: ')).strip()
            while nova_agenda == '':
                nova_agenda = str(input('Digite um nome valido: ')).strip()
            nova_agenda += '.pkl'
            criar_agenda(nova_agenda)
            agenda.salvar_contatos(nova_agenda)
            nova_agenda = agenda.verificar_agenda(nova_agenda)
            return nova_agenda
            
        
        elif resposta == 2:
            lista_de_agenda = glob.glob("./lista_de_agendas/*.pkl")
            if lista_de_agenda:
                
                return 'agendas listadas'
            else:
                print(cores("vermelho") + 'Você não tem agendas.' + cores("limpa"))
                return 'sem agendas'

        elif resposta == 3:
            print(f'\033[;32mSaindo...')
            quit() 
        else:
            linha()
            print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.' + cores("limpa"))
        
    def executar_comando_submenu(situacao_atual, resposta_submenu, agenda_selecionada, entrar_na_agenda):
        try:
            #pega o diretorio das agendas
            diretorio_agendas = selecionar_agendas()
            if len(diretorio_agendas) > 0:
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
                        else:
                            print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.' )
                            return ''
                            
                               
                    elif resposta_submenu == 2:
                        Interface.exibir_agendas()
                        linha()
                        selecionar_agenda = str(input('Digite o nome da agenda que deseja editar: ')) + '.pkl'
                        
                        if selecionar_agenda in diretorio_agendas:
                            novo_nome_agenda = str(input('Digite o novo nome da agenda: ')).strip()
                            while novo_nome_agenda == '':
                                novo_nome_agenda = str(input('Digite um nome valido: ')).strip()
                            novo_nome_agenda += '.pkl'
                            
                            os.rename("lista_de_agendas/" + selecionar_agenda, "lista_de_agendas/" +novo_nome_agenda)  
                            linha()
                            print(cores("verde") + 'Agenda atualizada!')
                            return ''
                            
                        else:
                            print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.' + cores("limpa"))
                            return ''
                    
                        
                    elif resposta_submenu == 3:
                        
                        caminho_do_diretorio = 'lista_de_agendas/'
                        lista_de_agenda = glob.glob("./lista_de_agendas/*.pkl")
                    
                        if lista_de_agenda:
                            try:
                                selecionar_agenda = str(input('Digite o nome da agenda que deseja remover: ')) + '.pkl'
                                os.unlink(caminho_do_diretorio + selecionar_agenda)
                                print(cores("verde") + 'Agenda removida!')
                                return ''
                                    

                            except FileNotFoundError:
                                print(cores("vermelho") + 'Essa agenda não existe.'+ cores("vermelho"))
                            
                        else:
                            linha()
                            print('\033[0;31mNão existem agendas ')
                            
                        return ''
                    
                    elif resposta_submenu == 4:
                        return 'agenda não selecionada'
                    else:
                        return 'Por favor digite um valor valido'
                    
            else:
                print(cores("vermelho") + 'Você não tem agendas' + cores("limpa"))
                return 'agenda não selecionada'

        except (IndexError):
            print('Por favor digite um valor válido' )
            
        while agenda_selecionada:   
            
            try:
                #CRIAR CONTATO
                if resposta_submenu == 1:
                    linha()
                    lista_contatos = Contato.criar_contatos()
                    linha()
                    contatos_existentes = agenda.verificar_agenda(agenda_selecionada)
                    contatos_existentes.extend(lista_contatos)
                    agenda.salvar_contatos(agenda_selecionada, contatos_existentes)
                    print(cores("verde") + 'Contato Adicionado.' + cores("limpa"))
                    
                    return agenda_selecionada

                #EDITAR CONTATO
                elif resposta_submenu == 2: 
                    try:
                        #exibe os contatos                    
                        agenda.exibir_contatos(agenda_selecionada)
                        
                        #pega a lista de contatos
                        contatos = agenda.pegar_contatos(agenda_selecionada)
                        
                        #verifica se existe items na lista
                        
                        if  len(contatos) > 0:
                            linha()
                            
                            #pergunta ao usuario qual contato ele deseja editar
                            index_contato = int(input('Qual o index do contato você deseja editar?'))
                            
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
                                    print(cores("vermelho") + 'ERRO:Por favor digite um valor válido.' + cores("limpa"))  
                                    
                                contatos_atualizados = agenda.editar_contatos(index_contato, contato_escolhido, contatos)
                                agenda.salvar_contatos(agenda_selecionada, contatos_atualizados)
                                return agenda_selecionada
                        else:
                            return agenda_selecionada
                    except:
                        print(cores("vermelho") + 'ERRO: Por favor digite um valor válido.' + cores("limpa"))
                    
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
                        print(cores("vermelho") + 'Você não tem contatos' + cores("limpa"))
                        return agenda_selecionada
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
        
        
            
