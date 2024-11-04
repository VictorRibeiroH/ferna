produto1 = "Camiseta"
valor_unitario1 = 30.0  

produto2 = "Calça"
valor_unitario2 = 50.0  


print(f"Produtos disponíveis:")
print(f"1. {produto1} - R$ {valor_unitario1:.2f} cada")
print(f"2. {produto2} - R$ {valor_unitario2:.2f} cada")

quantidade1 = int(input(f"Quantas unidades de {produto1} deseja comprar? "))
quantidade2 = int(input(f"Quantas unidades de {produto2} deseja comprar? "))

valor_total = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)

print(f'O valor da compra é:{valor_total}')