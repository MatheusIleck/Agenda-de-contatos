from agenda.agenda import Agenda
from contatos.contato import Contato
from funcoes import funcoes

agenda = Agenda()

class interface():
    def __init__(self, agenda, Contato):
        lista = agenda.verificar_agenda()


    def mostrar_comandos():
        funcoes.menu(['Criar Agenda','Exibir Agendas', 'Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir Agenda', 'Sair da Agenda'])
        
    def executar_comando(resposta):
        
        if resposta == 1:
            funcoes.linha()
            nova_agenda = str(input('Digite o nome da agenda que deseja criar: '))
            agenda.criar_agenda(nova_agenda)
        
        elif resposta == 2:
            Agenda.teste()
        
        elif resposta == 3:
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
            
            '''except(ValueError,TypeError):
                print(f'\033[;31mPor favor digite um valor válido.\033[m')
            
            except(IndexError):
                print(f'\033[;31mPor favor digite um valor válido.\033[m')'''
        
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
            agenda.exibir_contatos()
        
        elif resposta == 7:
            print(f'\033[;32mSaindo...\033[m')
            quit() 
        else:
            funcoes.linha()
            print(f'\033[;31mPor favor digite um valor válido.\033[m')
            
