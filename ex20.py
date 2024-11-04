valor_servico = 100.00
desconto = 20.00


idade = int(input("Digite sua idade: "))

if idade > 65 or idade < 18:
    valor_final = valor_servico - desconto
    print(f"Você tem direito ao desconto de R$ {desconto:.2f}.")
else:
    valor_final = valor_servico
    print("Você não tem direito ao desconto.")

print(f"O valor a ser pago pela passagem é R$ {valor_final:.2f}.")