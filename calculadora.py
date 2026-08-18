print("Calculadora Super Master Racer!!!")

while True:
    # Loop responsável por capturar os números inseridos pelo usuário
    while True:
        try:
            valor_user1 = float(input("Insira o primeiro valor: "))
            valor_user2 = float(input("Insira o segundo valor: "))
            break
        except ValueError:
            print("Insira apenas valores numéricos!")
    #Loop responsável por decidir qual operação matemática realizar
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
            if operacao == 1: # Soma
                total = valor_user1 + valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 2: # Subtração
                total = valor_user1 - valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 3: # Divisão
                # Tratamento específico para divisão por zero
                if valor_user2 == 0:
                    if valor_user1 == 0:
                        print("Indeterminação matemática! 0/0 não é definido!")
                else:
                    total = valor_user1 / valor_user2
                    print(f"O valor da sua conta é: {total}")
                    break
            elif operacao == 4: # Multiplicação
                total = valor_user1 * valor_user2
                print(f"O valor da sua conta é: {total}")
                break
            elif operacao == 5: # Escolher números novamente
                break
            elif operacao == 0: # Sair
                print("Até mais!!")
                exit(0)
            else:
                print("Escolha uma operação válida!")
        except ValueError:
            print("Digite uma operação válida!")

