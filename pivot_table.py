import pandas as pd

path = "data/file_example.xlsx"
data = pd.read_excel(path)

## Seleciona colunas específicas
data_frame = data[["Country", "Gender", "Age"]]

## Criando tabela pivô
pivot_table = data_frame.pivot_table(
    index = "Country",
    columns = "Gender",
    values = "Age",
    aggfunc = "sum"
)

print(pivot_table)

## Exportando tabela como arquivo Excel
file_name = "Output"
pivot_table.to_excel("data/pivot_table.xlsx", file_name)
