produtos = []
produtos.append(input("Digite o nome do produto 1: "))
produtos.append(input("Digite o nome do produto 2: "))
produtos.append(input("Digite o nome do produto 3: "))
produtos.append(input("Digite o nome do produto 4: "))

precos = []

precos.append(float(input("Digite o preço do produto 1: ")))
precos.append(float(input("Digite o preço do produto 2: ")))
precos.append(float(input("Digite o preço do produto 3: ")))
precos.append(float(input("Digite o preço do produto 4: ")))

print("Produtos:", produtos)
print("Preços:", precos)
print("Primeiro produto:", produtos[0], "Preço:", precos[0])
print("Último produto:", produtos[3], "Preço:", precos[3])
print("Valor total dos preços:", sum(precos))

produtos[0] = input("Digite o novo nome do produto 1: ")
print(produtos)