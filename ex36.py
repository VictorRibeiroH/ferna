n = int(input("Digite o número de termos da PA: "))


primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razão = float(input("Digite a razão da PA: "))


soma = 0


for i in range(n):
    termo_atual = primeiro_termo + i * razão  
    print(f"Termo {i + 1}: {termo_atual}")  
    soma += termo_atual  


print(f"A soma dos {n} termos da PA é: {soma:.2f}")