# Filtrando apenas transações acima de R$ 100 de forma concisa
transacoes = [50.0, 150.0, 200.0, 30.0, 500.0]
transacoes_altas = [valor for valor in transacoes if valor > 100.0]

print(transacoes_altas)  # [150.0, 200.0, 500.0]
