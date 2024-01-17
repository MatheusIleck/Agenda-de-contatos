def comandos(): 
    [
        {
          nome: "Criar nova agenda"
        },
        {
          nome: "Listar agendas existentes",
          sub_comandos: [
            {
              nome: "Selecionar agenda"
            },
            {
              nome: "Editar agenda"
            },
            {
              nome: "Deletar agenda"
            },
            {
              nome: "Voltar"
            }
          ]
        },
        {
          nome: "Editar agenda",
          sub_comandos: [
            {
              nome: "Selecionar agenda"
            },
            {
              nome: "Cancelar"
            }
          ]
        },
        {
          nome: "Deletar agenda",
          sub_comandos: [
            {
              nome: "Selecionar agenda"
            },
            {
              nome: "Cancelar"
            }
          ]
        },
        {
          nome: "Sair"
        }
      ]