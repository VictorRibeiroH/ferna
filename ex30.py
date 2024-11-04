x = int(input("Digite o valor de x (base): "))
n = int(input("Digite o valor de n (expoente): "))


resultado = 1


contador = 0  
while contador < abs(n):  
    resultado *= x  
    contador += 1  


if n < 0:
    resultado = 1 / resultado


print(f"O valor de {x} elevado a {n} é: {resultado}")