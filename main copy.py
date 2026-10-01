from datetime import datetime

menu = """" 

(1) Depositar
(2) Sacar
(3) Ver extrato
(4) Sair

"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque: "))
            if valor > 0 and valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saque inválido. Verifique o saldo, limite e se o valor é positivo.")
        else:
            print("Limite de saques atingido.")

    elif opcao == "3":
        print("\nExtrato:")
        print(extrato if extrato else "Nenhuma transação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def saudacao(nome):
    print(f"Olá, {nome}! Seu projeto no GitHub está funcionando perfeitamente.")

if __name__ == "__main__":
    saudacao("Dev")