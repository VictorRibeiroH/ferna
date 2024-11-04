numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

soma = numero1 + numero2
diferenca = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 !=0 else "Indefinido (divisão por zero)"

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")