produto = ()

produto = produto + (input("Digite o nome do produto 1: "),)
produto = produto + (input("Digite o nome do produto 2: "),)
produto = produto + (input("Digite o nome do produto 3: "),)
produto = produto + (input("Digite o nome do produto 4: "),)
precos = ()

precos = precos + (float(input("Digite o preço do produto 1: ")),)
precos = precos + (float(input("Digite o preço do produto 2: ")),)
precos = precos + (float(input("Digite o preço do produto 3: ")),)
precos = precos + (float(input("Digite o preço do produto 4: ")),)
quantidade = {
    "Produto 1": int(input("Digite a quantidade do produto 1: ")),
    "Produto 2": int(input("Digite a quantidade do produto 2: ")),
    "Produto 3": int(input("Digite a quantidade do produto 3: ")),
    "Produto 4": int(input("Digite a quantidade do produto 4: "))
}

print(produto[0], "Preço:", precos[0], "Quantidade:", quantidade["Produto 1"])
print(produto[1], "Preço:", precos[1], "Quantidade:", quantidade["Produto 2"])
print(produto[2], "Preço:", precos[2], "Quantidade:", quantidade["Produto 3"])
print(produto[3], "Preço:", precos[3], "Quantidade:", quantidade["Produto 4"])




























