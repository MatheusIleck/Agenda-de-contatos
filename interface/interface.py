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
            
        if resposta == 4:
            agenda.exibir_contatos()
        
            
    