from datetime import datetime
import re

saldo = 0 
banco_de_dados_usuarios = []
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o seu CPF: ")
    cpf_formatado = validar_formato_cpf(cpf)

    # 2. Verificação de unicidade
    if cpf_ja_cadastrado(cpf_formatado):
        raise ValueError(
            f"Erro: O CPF {cpf_formatado} já está registado no sistema."
        )
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário: ")
    
    usuario = {
        "id": len(banco_de_dados_usuarios) + 1,
        "nome": nome,
        "cpf": cpf_formatado,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    
    banco_de_dados_usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuario

def validar_formato_cpf(cpf: str) -> str:
    cpf_limpo = re.sub(r"\D", "", cpf)
    if len(cpf_limpo) != 11:
        raise ValueError("O CPF deve conter exatamente 11 dígitos.")
    return cpf_limpo


def cpf_ja_cadastrado(cpf: str) -> bool:
    return any(
        usuario["cpf"] == cpf for usuario in banco_de_dados_usuarios
    )

def criar_conta_corrente():
    global saldo, extrato, numero_saques, agencia, conta, usuario
    usuario = criar_usuario()
    agencia = "0001"
    conta = len(banco_de_dados_usuarios) + 1
    saldo = 0
    extrato = ""
    numero_saques = 0
    print("Conta criada com sucesso!")

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

menu = """
====================================
------------------------------------
====================================

    Bem-vindo ao Banco Python!

====================================
------------------------------------
====================================

        (1) Depositar
        (2) Sacar
        (3) Ver Extrato
        (4) Cadastrar Usuário
        (5) Criar Conta
        (6) Sair

====================================
------------------------------------
====================================
"""

while True:

    opcao = input(menu)

    if opcao == "1":
        depositar()

    elif opcao == "2":
        sacar()

    elif opcao == "3":
        ver_extrato()
        
    elif opcao == "4":
        criar_usuario()

    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")