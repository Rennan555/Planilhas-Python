import pandas as pd

## Importação do arquivo Excel
data = pd.read_excel("data/file_example.xlsx")

nCol = 20 ## Número de N colunas imprimidas (5 por assinatura padrão)

print(data.head(nCol)) ## N primeiras colunas
print(data.tail(nCol)) ## N últimas colunas

## Função para imprimir uma daterminada coluna do planilha (nome exato)
def print_collumn(col):
    print(data[col])
    print(data[col].value_counts()) ## Contagem de cada tipo repetido
