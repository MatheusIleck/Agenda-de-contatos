def criaContato(agenda):
    from utilitarios.utilitarios import leiaInt
    from contatos.contato import Contato
    continuar = 'S'
    while continuar in 'S':
        nome = str(input('Digite o Nome: '))
        numero = int(input('Digite o numero: '))
        pessoa = Contato(nome, numero)
        agenda.adicionarContato(pessoa)
        continuar = str(input('Deseja continuar: ')).upper()
        if continuar in 'N':
            break
