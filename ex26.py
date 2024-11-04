x = int(input("Digite o primeiro valor (X): "))
y = int(input("Digite o segundo valor (Y): "))


print("Escolha a ordem:")
print("1 - Ordem crescente")
print("2 - Ordem decrescente")
opcao = int(input("Digite sua opção (1 ou 2): "))

if opcao == 1:
    if x < y:
        print(f"Ordem crescente: {x}, {y}")
    else:
        print(f"Ordem crescente: {y}, {x}")
elif opcao == 2:
    if x > y:
        print(f"Ordem decrescente: {x}, {y}")
    else:
        print(f"Ordem decrescente: {y}, {x}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")