n = int(input("Digite o número de termos da PA: "))


primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razão = float(input("Digite a razão da PA: "))


termo_atual = primeiro_termo
soma = 0
contador = 0


while contador < n:
    print(f"Termo {contador + 1}: {termo_atual}")  
    soma += termo_atual  
    termo_atual += razão  
    contador += 1 


print(f"A soma dos {n} termos da PA é: {soma:.2f}")