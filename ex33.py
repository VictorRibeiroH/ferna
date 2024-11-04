x = int(input("Informe a quantidade de elementos que deseja inserir: "))


soma = 0
contador = 0


while contador < x:
    elemento = float(input(f"Digite o elemento {contador + 1}: "))  
    soma += elemento  
    contador += 1  


media = soma / x if x > 0 else 0  


print(f"A soma dos elementos é: {soma:.2f}")
print(f"A média dos elementos é: {media:.2f}")
