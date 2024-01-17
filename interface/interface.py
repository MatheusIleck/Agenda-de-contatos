from agenda.agenda import Agenda
from contatos.contato import Contato
from interface.utilidades import utilidades

# agenda = Agenda()

class Interface():
    def __init__(self, comandos, cor_principal):
       self.comandos = comandos
       self.cor_principal = cor_principal
        # agenda.verificar_agendas()
        # agenda.criar_arquivo()
        # lista = agenda.verificar_agenda()

    def mostrar_comandos():
        utilidades.menu(self.comandos)
        # utilidades.menu(['Adicionar Contato', 'Editar Contato', 'Remover Contato', 'Exibir agenda', 'Sair da Agenda'])
        
    # def executar_comando(resposta):
        # if resposta == 1:
        #     lista_contatos = Contato.criar_contatos()
        #     agenda.salvar_contatos(lista_contatos)
            
            
        # if resposta == 2:
        #     esperando_por_input = False
        #     try:
        #         agenda.exibir_contatos()
        #         contatos = agenda.pegar_contatos()
        #         if len(contatos) > 0:
        #             esperando_por_input = True
        #         while esperando_por_input == True:
        #             utilidades.linha()
        #             index_contato = int(input('Qual contato você deseja editar?'))
        #             contato_escolhido = agenda.encontrar_contato(index_contato)
        #             if contato_escolhido in contatos:
        #                 nome = utilidades.sanitizar_nome('Digite o Nome: ')
        #                 numero = utilidades.sanitizar_numero('Digite o Numero: ')
        #                 agenda.editar_contatos(index_contato, nome, numero)
        #                 agenda.salvar_contatos()
        #                 esperando_por_input = False
                        
        #     except(KeyboardInterrupt):
        #         print(f'\033[32mSaindo...\033[m')
            
        #     except(ValueError,TypeError):
        #         print(f'\033[;31mPor favor digite um valor válido.\033[m')
            
        #     except(IndexError):
        #         print(f'\033[;31mPor favor digite um valor válido.\033[m')
        
        
        # if resposta == 3:
        #     esperando_por_input = False
        #     try:
        #         agenda.exibir_contatos()
        #         contatos = agenda.pegar_contatos()
        #         if len(contatos) > 0:
        #             esperando_por_input = True
        #         while esperando_por_input == True:
        #             utilidades.linha()
        #             index_contato = int(input('Qual contato você deseja remover?'))
        #             contato_escolhido = agenda.encontrar_contato(index_contato)
        #             if contato_escolhido in contatos:    
        #                 agenda.remover_contatos(index_contato)
        #                 agenda.salvar_contatos()
        #                 esperando_por_input = False
                        
        #     except (ValueError,TypeError):
        #         print(f'\033[;31mPor favor digite um valor válido\033[m')
        #     except KeyboardInterrupt:
        #         print(f'\033[;32mSaindo...\033[m')
        #     except(IndexError):
        #         print(f'\033[;31mPor favor digite um valor válido.\033[m')
        
        # if resposta == 4:
        #     agenda.exibir_contatos()
        
        
        # if resposta == 5:
        #     print(f'\033[;32mSaindo...\033[m')
        #     quit()
            
    