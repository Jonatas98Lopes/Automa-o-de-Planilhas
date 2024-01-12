import openpyxl

print('Bem-vindo ao gerador de planilhas!')
print('Para começar, vamos criar uma nova página dentro de uma planilha.')

workbook = openpyxl.Workbook()
del workbook['Sheet']

while True:
    new_sheet_name = input('Digite o nome da página: ')
    workbook.create_sheet(new_sheet_name)
    
    add_another_sheet = input('Criar mais uma página nesta planilha?(s/n): ')
    if add_another_sheet == 'n':
        break

# Apenas para teste da planilha
workbook.save('dados.xlsx')