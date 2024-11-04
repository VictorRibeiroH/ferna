n = int(input("Digite a quantidade de números que deseja inserir: "))

quantidade_pares = 0
quantidade_impares = 0

for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))  

    if numero % 2 == 0:
        quantidade_pares += 1  
    else:
        quantidade_impares += 1  

print(f"A quantidade de números pares é: {quantidade_pares}")
print(f"A quantidade de números ímpares é: {quantidade_impares}")