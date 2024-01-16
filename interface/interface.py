from agenda.agenda import Agenda
from contatos.contato import Contato
from funções import funções

agenda = Agenda()

class interface():
    def __init__(self, agenda, Contato):
        agenda.criar_arquivo()
        lista = agenda.verificar_agenda()


    def mostrar_comandos():
        funções.menu(['Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir agenda', 'Sair da Agenda'])
        
    def executar_comando(resposta):
        if resposta == 1:
            lista_contatos = Contato.criar_contatos()
            agenda.salvar_contatos(lista_contatos)
            
            
        if resposta == 2:
            esperando_por_input = False
            try:
                agenda.exibir_contatos()
                contatos = agenda.pegar_contatos()
                if len(contatos) > 0:
                    esperando_por_input = True
                while esperando_por_input == True:
                    funções.linha()
                    index_contato = int(input('Qual contato você deseja editar?'))
                    contato_escolhido = agenda.encontrar_contato()
                    if contato_escolhido in contatos:
                        nome = funções.sanitizar_nome('Digite o Nome: ')
                        numero = funções.sanitizar_numero('Digite o Numero: ')
                        agenda.editar_contatos(index_contato, nome, numero)
                        agenda.salvar_contatos()
                        esperando_por_input = False
            except(KeyboardInterrupt):
                print(f'\033[32mSaindo...\033[m')
            except (ValueError,TypeError):
                print(f'\033[;31mErro: O usuario informou um dado inválido\033[m')
            
        if resposta == 4:
            agenda.exibir_contatos()
        
        if resposta == 3:
            try:
                agenda.exibir_contatos()
                agenda.remover_contatos()
                agenda.salvar_contatos()
                
            except (ValueError):
                print(f'\033[;31mPor favor digite um valor valido\033[m')
            except KeyboardInterrupt:
                print(f'\033[;32mSaindo...\033[m')
        
        if resposta == 5:
            print(f'\033[;32mSaindo...\033[m')
            quit()
            
    