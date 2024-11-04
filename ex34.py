x = int(input("Informe a quantidade de elementos que deseja inserir: "))


soma = 0


for i in range(x):
    elemento = float(input(f"Digite o elemento {i + 1}: "))  


media = soma / x if x > 0 else 0  


print(f"A soma dos elementos é: {soma:.2f}")
print(f"A média dos elementos é: {media:.2f}")