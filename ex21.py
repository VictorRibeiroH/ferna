letra = input("Digite uma letra: ").strip()


if len(letra) == 1 and letra.isalpha():
    if letra in "AEIOU":
        print("Vogal maiúscula")
    elif letra in "aeiou":
        print("Vogal minúscula")
    else:
        print("Consoante")
else:
    print("Entrada inválida! Por favor, digite uma única letra do alfabeto.")