print("Calculadora Super Master Racer!!!")

while True:
    while True:
        try:
            valor_user1 = float(input("Insira o primeiro valor: "))
            valor_user2 = float(input("Insira o segundo valor: "))
            break
        except ValueError:
            print("Insira apenas valores numéricos!")
        #print(f"Valor 1: {valor_user1}. Valor 2: {valor_user2}")
    while True:
        try:
            print('''
            1 - Soma
            2 - Subtração
            3 - Divisão
            4 - Multiplicação
            5 - Escolher números novamente
            0 - Sair
            ''')
            operacao = int(input("Escolha a operação: "))
            total = 0
            if operacao == 1:
                total = valor_user1 + valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 2:
                total = valor_user1 - valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 3:
                total = valor_user1 / valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 4:
                total = valor_user1 * valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 5:
                break
            elif operacao == 0:
                print("Até mais!!")
                exit(0)
            else:
                print("Escolha uma operação válida!")
        except ValueError:
            print("Digite uma operação válida!")

