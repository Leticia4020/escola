cliente = []
pet = []
servico = []
opcao = 8
while opcao != 0:
    print("=== SISTEMA PETSHOP ===")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar Pet")
    print("3 - Listar clientes")
    print("4 - Listar Pets")
    print("5 - Registrar serviço")
    print("6 - Exibir Relatório")
    print("7 - Buscar pet")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("=== CADASTRO CLIENTE ===")
        cliente_nome = input("Digite o nome do cliente: ")
        cliente_telefone = input("Digite o telefone do cliente: ")
        cliente.append((cliente_nome, cliente_telefone))
        print("\nCliente cadastrado com sucesso!")
    elif opcao == 2:
        print("=== CADASTRAR PET ===")
        pet_nome = input("Digite o nome do pet: ")
        pet_raca = input("Digite a raça do pet: ")
        pet_dono = input("Digite o nome do dono do pet: ")
        pet.append((pet_nome, pet_raca, pet_dono))
        print("\nPet cadastrado com sucesso!")
    elif opcao == 3:
        print("=== LISTA DE CLIENTES ===")
        for c in cliente:
            print(f"Cliente: {c[0]}, Telefone: {c[1]}")
    elif opcao == 4:
        print("=== LISTA DE PETS ===")
        for p in pet:
            print(f"Pet: {p[0]}, Raça: {p[1]}, Dono: {p[2]}")
    elif opcao == 5:
        print("=== REGISTRAR SERVIÇO ===")
        
        servico = {
            "Banho": 80.0,
            "Tosa": 100.0,
            "Consulta": 120.0,
            "Hospedagem": 150.0
        } 
        print(servico)
        servico_nome = input("Digite o nome do serviço (Banho, Tosa, Consulta, Hospedagem): ")
        if servico_nome in servico:
            servico_valor = servico[servico_nome]
            print(f"Valor do serviço '{servico_nome}': R${servico_valor:.2f}")
        pet.append((servico_nome, servico_valor))

        print("\nServiço registrado com sucesso!")
    elif opcao == 6:
        print("=== RELATÓRIO ===")
        print(f"Total de clientes: {len(cliente)}")
        print(f"Total de pets: {len(pet)}")
        print(f"Total de serviços registrados: {len(servico)}")
        print("\nFaturamento total: R$",servico_valor:.2f)
    elif opcao == 7:
        pet_busca = input("Digite o nome do pet a ser buscado: ")
        encontrado = False
        for p in pet:
            if p[0] == pet_busca:
                print(f"Pet encontrado: {p[0]}, Raça: {p[1]}, Dono: {p[2]}")
                encontrado = True
                break
        if not encontrado:
            print("Pet não encontrado.")                
    elif opcao == 0:
        print("Saindo do programa. Até mais!")
    else:
        print("Opção inválida. Por favor, tente novamente.")