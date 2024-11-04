produtos = {
    1: ("Produto A", 10.00),
    2: ("Produto B", 20.00),
    3: ("Produto C", 30.00),
    4: ("Produto D", 40.00),
    5: ("Produto E", 50.00),
}

while True:
    
    print("Tabela de Produtos:")
    print("Código\tNome do Produto\tPreço Unitário")
    for codigo, (nome, preco) in produtos.items():
        print(f"{codigo}\t{nome}\t\tR$ {preco:.2f}")

    
    codigo_produto = int(input("Digite o código do produto que deseja comprar: "))
    quantidade = int(input("Digite a quantidade comprada: "))

    if codigo_produto in produtos:
        nome_produto, preco_unitario = produtos[codigo_produto]
        preco_total = preco_unitario * quantidade
        print(f"O total a pagar pelo(a) {nome_produto} é: R$ {preco_total:.2f}")
    else:
        print("Código de produto inválido!")

    
    repetir = input("Deseja repetir a operação? (0 - Sair, 1 - Repetir): ")
    if repetir != '1':
        break