menu = """ \n
==== MENU ====
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
exercicio_sistema_bancario_python
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if  opcao == "d":
        valor = float(input("informe o valor do depósito: "))
        
        if valor > 0:
            saldo  +=  valor
            extrato  +=  f"Depósito: \t R$ {valor :.2f} \n "
            print (" \n ===Depósito realizado com sucesso! ===")

        else: print ( " \n Operação falhou! O valor informado é inválido." )
       
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        excedeu_saldo  =  valor  >  saldo
        excedeu_limite  =  valor  >  limite
        excedeu_saques  =  numero_saques  >=  LIMITE_SAQUES

        if excedeu_saldo:
            print ( " \n Operação falhou! Você não tem saldo suficiente." )

        elif excedeu_limite:
            print ( " \n Operação falhou! O valor do saque excede o limite." )

        elif excedeu_saques:
            print ( " \n Operação falhou! Número máximo de saques excedido." )

        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: \t R$ {valor :.2f} \n"
            numero_saques += 1
            print(" \n === Saque realizado com sucesso! ===")

        else:
            print( " \n Operação falhou! O valor informado é inválido." )

    elif opcao == "e":
        print(" \n =============== EXTRATO ===============")
        print("Não foram realizadas movimentações."  if  not  extrato  else  extrato)
        print(f" \n Saldo: \t R$ { saldo :.2f}")
        print("=========================================")

    elif  opcao  ==  "q":
        print("Você saiu da sua conta!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")