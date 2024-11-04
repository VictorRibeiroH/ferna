import math

altura=int(input('Digite um valor para altura:'))
raio=int(input('Digite um valor para raio:'))

Area=int(math.pi*raio**2)
Volume=int(math.pi*raio**2*altura)


print(f'A area do cilindro é {Area}')
print(f'O volume do cilindro é: {Volume}')