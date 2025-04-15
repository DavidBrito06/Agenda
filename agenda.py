def adicionar_contato(agenda, nome_contato, numero_contato, email_contato,):
    contato = {
        "nome": nome_contato,
        "numero": numero_contato,
        "email": email_contato,
        "favorito": False
    }
    agenda.append(contato)
    print(f"Contato '{nome_contato}' adicionado com sucesso!")
    return


def ver_contatos(agenda):
    print("\nLista de contatos:")
    if not agenda:
        print("Nenhum contato na agenda.")
        return
    for indice, contato in enumerate(agenda):
        favorito = "Sim" if contato["favorito"] else "Não"
        print(f"{indice + 1}. {contato['nome']} - {contato['numero']} - {contato['email']} - Favorito: {favorito}")


def atualizar_contato(agenda, indice_contato, novo_nome, novo_numero, novo_email):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
       agenda[indice_ajustado]["nome"] = novo_nome
       agenda[indice_ajustado]["numero"] = novo_numero
       agenda[indice_ajustado]["email"] = novo_email
       print(f"Contato '{novo_nome}' atualizado com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")
    return

def adicionar_com_favorito(agenda, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        agenda[indice_ajustado]["favorito"] = True
        print(f"Contato '{agenda[indice_ajustado]['nome']}' adicionado como favorito!")
    else:
        print("Índice inválido. Contato não encontrado.")


def remover_contato(agenda, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        contato_removido = agenda.pop(indice_ajustado)
        print(f"Contato '{contato_removido['nome']}' removido com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")
    return


agenda = []
while True:
    print("\n Menu da agenda")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Atualizar contato")
    print("4 - Adicionar com favorito")
    print("5 - Remover contatos")
    print("6 - Sair da agenda")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":	
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        numero_contato = input("Digite o número do contato: ")
        email_contato = input("Digite o email do contato: ")
        adicionar_contato(agenda, nome_contato, numero_contato, email_contato)	
    elif escolha == "2":
        ver_contatos(agenda)
    elif escolha == "3":
        ver_contatos(agenda)
        indice_contato = int(input("Digite o número do contato que deseja atualizar: "))
        novo_nome = input("Digite o novo nome do contato: ")
        novo_numero = input("Digite o novo número do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        atualizar_contato(agenda, indice_contato, novo_nome, novo_numero, novo_email)
    elif escolha == "4":
        ver_contatos(agenda)
        indice_contato = int(input("Digite o número do contato que deseja adicionar como favorito: "))
        adicionar_com_favorito(agenda, indice_contato)
    elif escolha == "5":
        ver_contatos(agenda)
        indice_contato = int(input("Digite o número do contato que deseja remover: "))
        remover_contato(agenda, indice_contato)
    elif escolha == "6": 
        print("Saindo da agenda...")
        break