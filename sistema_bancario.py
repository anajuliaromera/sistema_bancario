menu = """
---------- Seja Bem-vindo ao sistema bancário ----------

Digite a letra da opção que deseja realizar:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")

    elif opcao == "s":
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite_diario
        excedeu_saques = valor >= limite_saque

        valor = float(input("Informe o valor que deseja sacar: "))

        if excedeu_saldo:
            print("Operação negada, seu saldo é insuficiente! ")

        elif excedeu_limite:
            print("Operação falhou, limite diário atingido! ")
        
        elif excedeu_saques:
            print("Operação falhou, limite de saques atingido! ")
        
        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1
        
        else: 
            print("Operação falhou, valor informado é inválido")

    elif opcao == "e":
        print("\n ---------------- EXTRATO ----------------")
        print("Nenhuma operação foi realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------")
    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada!")
