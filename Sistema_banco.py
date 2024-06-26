menu = """
  ---------- M E N U ----------
  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [4] - Sair
  -----------------------------
  """



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Informe o valor que deseja Depositar: R$ "))
        if valor > 0:
            print("Depósito realizado com sucesso!")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor Inválido\n")
    
    elif opcao == 2:
        print(f"SALDO ATUAL: R$ {saldo}")
        valor_saque = float(input("Digite o valor que deseja sacar (máximo 500) : R$ "))
        if numero_saques >= LIMITE_SAQUES:
            print("Você já ultrapassou o número de saques diários (3),\nTente novamente amanha\n")
        elif valor_saque > 500 or valor_saque < 0:
            print("Valor Inválido\n")
        elif valor_saque > saldo:
            print("Saldo Insuficiente para realizar essa transição\n")
        else:
            print("Saque realizado com Sucesso!")
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"

    elif opcao == 3:
        print(f">>> Extrato Bancário <<< \n {extrato}")
        print(f"Saldo Atual: {saldo}")
    
    elif opcao == 4:
        break
    else:
        
        print("Número de opção inválida\n")



