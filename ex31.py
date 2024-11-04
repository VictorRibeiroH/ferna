numero = float(input("Digite um número: "))


contagem_divisoes = 0


while numero >= 1:
    numero /= 2  
    contagem_divisoes += 1  

 
print(f"O resultado da última divisão é: {numero:.6f}")
print(f"Quantidade de divisões efetuadas: {contagem_divisoes}")