from openpyxl import load_workbook

## Ler pasta de trabalho
work_book = load_workbook("data/pivot_table.xlsx")
sheet = work_book["Output"]

## Acessando uma célula específica
print(sheet["B2"].value)

def column_iteration(col):
    for i in range(2,5):
        country = sheet["A%s" %i].value
        out = sheet[col + "%s" %i].value
        print("A soma de {0} foi de {1}".format(country, out))

column_iteration("B") ## Female
column_iteration("C") ## Male
