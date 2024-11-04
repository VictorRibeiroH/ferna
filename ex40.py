
n = int(input("Digite a quantidade de números que deseja inserir: "))


quantidade_pares = 0
quantidade_impares = 0


contador = 0


while contador < n:
    numero = int(input(f"Digite o número {contador + 1}: "))  # Lê o número
    
    if numero % 2 == 0:
        quantidade_pares += 1  
    else:
        quantidade_impares += 1 

    contador += 1  

print(f"A quantidade de números pares é: {quantidade_pares}")
print(f"A quantidade de números ímpares é: {quantidade_impares}")