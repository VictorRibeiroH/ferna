if numero % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "zero"

print(f"O número é {par_impar} e {sinal}.")