from datetime import datetime

def depositar():
    global saldo, extrato
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        hora_atual = datetime.now().strftime("%H:%M:%S de %d/%m/%Y")
        extrato += f"Depósito: R$ {valor:.2f} — {hora_atual}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso às {hora_atual}!")
    else:
        print("Valor inválido. O depósito deve ser maior que zero.")

def sacar():
    global saldo, numero_saques, extrato
    if numero_saques < LIMITE_SAQUES:
        valor = float(input("Digite o valor do saque: "))
        if valor > 0 and valor <= saldo and valor <= limite:
            saldo -= valor
            numero_saques += 1
            hora_atual = datetime.now().strftime("%H:%M:%S de %d/%m/%Y")
            extrato += f"Saque: R$ {valor:.2f} — {hora_atual}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso às {hora_atual}!")
        else:
            print("Saque inválido. Verifique o saldo, limite e se o valor é positivo.")
    else:
        print("Limite total de saques diários atingido.")

def ver_extrato():
    global extrato, saldo, numero_saques, LIMITE_SAQUES
    print("\nExtrato:")
    print(extrato if extrato else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    print(f"Você realizou {numero_saques} saques hoje. Limite de saques diários: {LIMITE_SAQUES}.\n")

menu = """Bem-vindo ao Desafio do Banco de Datas!
Por favor, selecione uma opção:
(1) Depositar
(2) Sacar
(3) Ver Extrato
(4) Sair

"""
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

while True:

    opcao = input(menu)

    if opcao == "1":
        depositar()

    elif opcao == "2":
        sacar()

    elif opcao == "3":
        ver_extrato()
        
    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")