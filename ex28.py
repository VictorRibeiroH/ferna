produtos = {
    1: 10.00,
    2: 20.00,
    3: 30.00,
    4: 40.00,
    5: 50.00,
}


total_vendas = 0.0

print("Digite os pares de números (número do produto e quantidade).")
print("Digite -1 para encerrar a entrada.")

while True:
    
    codigo_produto = int(input("Número do Produto: "))
    
    
    if codigo_produto == -1:
        break

    
    quantidade_vendida = int(input("Quantidade vendida em um dia: "))

    
    if codigo_produto in produtos:
        preco_unitario = produtos[codigo_produto]
        total_vendas += preco_unitario * quantidade_vendida
    else:
        print("Código de produto inválido!")


print(f"O valor total a varejo de todos os produtos vendidos na semana passada é: R$ {total_vendas:.2f}")