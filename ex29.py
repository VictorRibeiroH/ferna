while True:
    
    nome = input("Digite o nome do atleta: ")
    idade = int(input("Digite a idade do atleta: "))

    
    if 5 <= idade <= 10:
        categoria = "Infantil"
    elif 11 <= idade <= 15:
        categoria = "Juvenil"
    elif 16 <= idade <= 20:
        categoria = "Junior"
    elif 21 <= idade <= 25:
        categoria = "Profissional"
    else:
        categoria = "Fora da faixa etária para classificação"

    
    print(f"O atleta {nome} está na categoria: {categoria}")

    
    repetir = input("Deseja repetir a operação? (0 - Sair, 1 - Repetir): ")
    if repetir != '1':
        break