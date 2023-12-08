import pandas as pd

## Importação do arquivo Excel
path = "data/file_example.xlsx"
data = pd.read_excel(path)

nCol = 20 ## Número de N colunas imprimidas (5 por assinatura padrão)

print(data) ## Imprime a tabela inteira
print(data.head(nCol)) ## N primeiras colunas
print(data.tail(nCol)) ## N últimas colunas

## Função para imprimir uma daterminada coluna do planilha (nome exato)
def print_column(col):
    print(data[col])
    print(data[col].value_counts()) ## Contagem de cada tipo repetido
