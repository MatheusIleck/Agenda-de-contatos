import pickle


from utilitarios.utilitarios import menu
from contatos.contato import Contato
from agenda.agenda import Agenda
from Funções.funções import cria_contato


agenda = Agenda()
agenda.cria_arquivo()

while True:
    resp = menu(['Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir agenda', 'Sair da Agenda'])
    if resp == 1:
        cria_contato(agenda)
    elif resp == 2:
        agenda.edita_contato()
    elif resp == 3:
        agenda.remove_contato()
    elif resp == 4:
        agenda.exibe_contato()
    elif resp == 5:
        break
    else:
        print(f'Por favor digite um valor valido')
