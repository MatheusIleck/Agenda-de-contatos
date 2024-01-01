import pickle
from utilitarios.utilitarios import menu
from contatos.contato import Contato
from agenda.agenda import Agenda
from Funções.funções import criaContato
agenda = Agenda()
agenda.criaArquivo()
continuar = 'S'
while True:
    resp = menu(['Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir agenda', 'Sair da Agenda'])
    if resp == 1:
        criaContato(agenda)
    if resp == 2:
        print('Editar contato')
    if resp == 3:
        print('Remover contato')
    if resp == 4:
        agenda.exibeContato()
    if resp == 5:
        break

