#3) Análise de Faturamento Diário em Python (usando JSON):
import json

# Carregando dados do faturamento diário de um arquivo JSON
with open("faturamento_diario.json", "r") as f:
    faturamento_diario = json.load(f)

# Calculando o menor e o maior valor de faturamento
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calculando a média mensal, ignorando dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculando o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

# Imprimindo os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")