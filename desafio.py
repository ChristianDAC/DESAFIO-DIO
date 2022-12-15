menu = """
[d] depositar
[s] sacar
[e] extrato 
[q] sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    opcao = input(menu)
    

    if opcao == "d":
        valor = float(input("informe o valor do deposito :  "))
        
        if valor > 0:
            saldo += valor
            extrato += f"deposito : R${valor:.2f}\n"
        else:
            print("operacao falhou, informe um valor valido ")

    

    elif opcao == "s":

        valor = float(input("informe o valor do saque : "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("opracao falhou, limite de saldo excedido")
        elif excedeu_limite:
            print("operacao falhou, limite ecxedido")
        elif excedeu_saques:
            print("operacao falhou, numero de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("operacao falhou, informar um valor valido")



    elif opcao == "e":
        print("\n========== EXTRATO==========")
        print("nao forao realizados movimentacoes." if not extrato else extrato)
        print(f"\nSALDO: R${saldo:.2f}")
        print("==============================")
        
        


    elif opcao == "q":
        break
    else:
        print("opcao invalida, por favor digite a opcao desejada ")
