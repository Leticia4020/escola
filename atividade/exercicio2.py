estoque = []

estoque.append(int(input("Digite a quantidade do produto 1: ")))
estoque.append(int(input("Digite a quantidade do produto 2: ")))
estoque.append(int(input("Digite a quantidade do produto 3: "))) 
estoque.append(int(input("Digite a quantidade do produto 4: ")))

print("Produto 1:", estoque[0], "Produto 2:", estoque[1],
      "Produto 3:", estoque[2], "Produto 4:", estoque[3])
print("Primeiro produto:", estoque[0])
print("Último produto:", estoque[3])
print("Valor total do estoque:", sum(estoque))
