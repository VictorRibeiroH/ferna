n = int(input("Digite a quantidade de números que deseja inserir: "))


maior = None
menor = None


for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))  
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero


print(f"O maior número informado é: {maior}")
print(f"O menor número informado é: {menor}")