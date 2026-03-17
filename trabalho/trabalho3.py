def buscar_pet(lista):
    pet_busca = input("Digite o nome do pet a ser buscado: ")
    pet_encontrado = None

    for pet in lista:
        if pet["nome"].lower() == pet_busca.lower():
            print(f"Pet encontrado: {pet['nome']} (CPF: {pet['cpf']})")
            pet_encontrado = pet
            break

    return pet_encontrado


servico = {
    1: {"nome": "Banho", "valor": 80.00},
    2: {"nome": "Tosa", "valor": 100.00},
    3: {"nome": "Consulta", "valor": 120.00},
    4: {"nome": "Hospedagem", "valor": 150.00},
}

servicos_realizados = []


def registrar_servico(lista):

    print("=== REGISTRAR SERVIÇO ===")

    pet = buscar_pet(lista)

    if not pet:
        print("Pet não encontrado.\n")
        return

    print("\n=== SERVIÇOS DISPONÍVEIS ===")

    for i in servico:
        s = servico[i]
        print(f"{i}. {s['nome']} - R$ {s['valor']:.2f}")

    while True:

        opcao = int(input("Escolha o número do serviço: "))

        if opcao == 0:
            print("Voltando ao menu principal.")
            return

        if opcao in servico:

            servico_escolhido = servico[opcao]

            print("\n=== SERVIÇO REGISTRADO ===")
            print(f"Pet: {pet['nome']}")
            print(f"CPF do dono: {pet['cpf']}")
            print(f"Serviço: {servico_escolhido['nome']}")
            print(f"Valor: R$ {servico_escolhido['valor']:.2f}")

            servicos_realizados.append({
                "pet": pet["nome"],
                "cpf_dono": pet["cpf"],
                "servico": servico_escolhido["nome"],
                "valor": servico_escolhido["valor"]
            })

            continuar = input("\nDeseja registrar outro serviço para este pet? (s/n): ")

            if continuar.lower() != "s":
                print("\n=== SERVIÇOS REGISTRADOS PARA ESTE PET ===")
                total = 0
                for s in servicos_realizados:
                     if s["pet"] == pet["nome"] and s["cpf_dono"] == pet["cpf"]:
                          print(f"Pet: {s['pet']}")
                          print(f"CPF dono: {s['cpf_dono']}")
                          print(f"Serviço: {s['servico']}")
                          print(f"Valor: R$ {s['valor']:.2f}")
                          print("----------------------")
                          total += s["valor"]
                          print(f"VALOR TOTAL: R$ {total:.2f}")
                break

        else:
            print("Opção inválida.")


def relatorios(clientes, pets):

    print("\n=== RELATÓRIOS ===")

    total_clientes = len(clientes)
    total_pets = len(pets)
    total_servicos = len(servicos_realizados)

    faturamento_total = 0

    for s in servicos_realizados:
        faturamento_total += s["valor"]

    print(f"Total de clientes cadastrados: {total_clientes}")
    print(f"Total de pets cadastrados: {total_pets}")
    print(f"Total de serviços realizados: {total_servicos}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")


def relatorio_clientes(clientes):

    print("\n=== RELATÓRIO DE CLIENTES ===")

    for cliente in clientes:

        print(f"\nCliente: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")

        encontrou_servico = False

        for s in servicos_realizados:

            if s["cpf_dono"] == cliente["cpf"]:

                print(f"Pet: {s['pet']}")
                print(f"Serviço realizado: {s['servico']}")
                print(f"Valor: R$ {s['valor']:.2f}")
                print("----------------------")

                encontrou_servico = True

        if not encontrou_servico:
            print("Nenhum serviço realizado.")

