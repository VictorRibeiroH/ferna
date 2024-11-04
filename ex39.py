S = 0  
numerador = 1  
denominador = 1  


while denominador <= 50:
    S += numerador / denominador 
    numerador += 2  
    denominador += 1  


print(f"O valor de S é: {S:.4f}")