n = int(input("Digite um número inteiro para calcular seu fatorial: "))


fatorial = 1


if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    
    contador = 1
    

    while contador <= n:
        fatorial *= contador  
        contador += 1  

    
    print(f"O fatorial de {n} é: {fatorial}")