import json

def ler_faturamento(caminho_arq):
    with open(caminho_arq, 'r') as arq:
        dados = json.load(arq)
    return dados['faturamento_diario']

def calcular_faturamento(faturamento):
    faturamento_filtrado = [valor for valor in faturamento if valor > 0]

    menor = min(faturamento_filtrado)
    maior = max(faturamento_filtrado)

    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

    nro_dias_superior_media = len([valor for valor in faturamento if valor > media_mensal])

    return menor, maior, nro_dias_superior_media

faturamento = ler_faturamento('dados.json')

menor, maior, nro_dias_superior_media = calcular_faturamento(faturamento)

print(f"Menor faturamento do mês: {menor}")
print(f"Maior faturamento do mês: {maior}")
print(f"Número de dias com faturamento acima da média: {nro_dias_superior_media}")
