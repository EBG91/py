# Variáveis iniciais e menu de opções
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>
"""

saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saque
extrato = []  # Lista para armazenar o histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Limite diário de saques

#Lógica principal do menu
while True:
    opcao = input(menu)  #Exibe o menu e lê a opção escolhida pelo usuário

    if opcao == "1":
        #Depósito
        print("Depósito")
        deposito = input("Digite o valor do depósito: ")  # Lê o valor do depósito
        
        #Verificação para garantir que o valor do depósito é positivo
        while not (deposito.replace(".", "", 1).isdigit() and float(deposito) > 0):
            print("Valor inválido, digite um valor positivo.")
            deposito = input("Digite o valor do depósito: ")  #Pede novo valor caso o anterior seja inválido
        
        deposito = float(deposito)  #Converte o valor válido para float
        saldo += deposito  #Adiciona o valor do depósito ao saldo
        extrato.append(f"Depósito: R$ {deposito:.2f}")  #Adiciona a transação ao extrato
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")  #Mostra o valor do depósito

    elif opcao == "2":
        #Saque
        print("Saque")
        saque = input("Digite o valor do saque: ")  #Lê o valor do saque
        
        #Verificação para garantir que o valor do saque é positivo
        while not (saque.replace(".", "", 1).isdigit() and float(saque) > 0):
            print("Valor inválido, digite um valor positivo.")
            saque = input("Digite o valor do saque: ")  # Pede novo valor caso o anterior seja inválido
        
        saque = float(saque)  # Converte o valor válido para float

        # Verificações para validar o saque
        if saque > saldo:
            print("Saldo insuficiente.")  # Caso o saque seja maior que o saldo disponível
        elif saque > limite:
            print("Limite de saque excedido.")  # Caso o saque seja maior que o limite permitido
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários excedido.")  # Caso o número de saques diários tenha sido atingido
        else:
            saldo -= saque  # Deduz o valor do saque do saldo
            extrato.append(f"Saque: R$ {saque:.2f}")  # Adiciona a transação ao extrato
            numero_saques += 1  # Incrementa o contador de saques
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")  # Confirmação de saque

    elif opcao == "3":
        # Opção de extrato
        print("\n================ EXTRATO ================")
        if not extrato:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações.")  # Caso não haja transações
        else:
            for transacao in extrato:
                print(transacao)  # Exibe cada transação do extrato
        print(f"Saldo atual: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("=========================================")    
    elif opcao == "0":
        # Opção para sair do programa
        break

    else:
        print("Operação inválida, verifique a opção no menu e tente novamente.")  # Mensagem para opção inválida
