from agenda.agenda import Agenda
from contatos.contato import Contato
from funções import funções

agenda = Agenda()

class interface():
    def __init__(self, agenda, Contato):
        agenda.criar_arquivo()
        agenda.verificar_agenda()


    def mostrar_comandos():
        funções.menu(['Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir agenda', 'Sair da Agenda'])
        
    def executar_comando(resposta):
        if resposta == 1:
            lista_contatos = Contato.criar_contatos()
            agenda.salvar_contatos(lista_contatos)
            
            
        if resposta == 2:
            try:
                agenda.exibir_contatos()
                agenda.editar_contatos()
                agenda.salvar_contatos()
            except(KeyboardInterrupt):
                print(f'\033[32mSaindo...\033[m')
            
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
            
    