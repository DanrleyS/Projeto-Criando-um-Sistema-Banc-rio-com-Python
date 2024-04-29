#SISTEMA BANCÁRIO

menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

"""

user = "Dan"
saldo = 1000 
limite_valor = 500
limite_saques = 3
numero_saques = 0
deposito = 0 
saque = 0
extrato = ""

while True:
    opcao = input(menu)

    if opcao == "1":
        print("---------------Deposito---------------")
        deposito = float (input ("informe o valor que deseja depositar:\n "))
        if deposito >= 0:
            print(f"R$ {deposito:.2f}")
            saldo = (saldo + deposito)
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"operação feita, novo saldo R$ {saldo:.2f}")
            
        else:
            print("Operação restrita: valor inválido. Voltando ao menu")
        
   
    elif opcao == "2":
        print("---------------Saque---------------")
        print(f"Saldo disponivel R$  {saldo:.2f}")
        saque = float (input("informe o valor desejado para saque:\n "))
        if saque > saldo:
            print ("Saldo indisponível. Voltando ao menu")
        elif saque <= saldo and saque <= limite_valor:
            if numero_saques < limite_saques:
                print("saque efetuado, retire o dinheiro no caixa")
                saldo = (saldo - saque)
                numero_saques = numero_saques + 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"numero de saques realizados" , numero_saques)
            elif numero_saques >= limite_saques:
                print(f"numero de saques atingido. saques realizados: " , numero_saques , "de " , limite_saques )


        elif saque <= saldo and saque >= limite_valor:
            print("limite indisponivel, voltando ao menu")
        

    elif opcao == "3":
        print("---------------Extrato---------------")
        if deposito > 0 or saque > 0:
            print(extrato)
            print(f"saldo atual R$ {saldo:.2f}\n")
        else:
            print("não foram realizadas operações")
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada")