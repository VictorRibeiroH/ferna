nota1= float(input('Digite uma nota:'))
nota2= float(input('Digite uma nota:'))
nota3= float(input('Digite uma nota:'))
nota4= float(input('Digite uma nota:'))
presença=int(input('Número de presenças:'))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >=6 and  presença >=20:
    print('Aprovado')
elif 5<= media <= 5.9 and presença >= 20:
    print('Dependência')
else:
    print('Reprovado')