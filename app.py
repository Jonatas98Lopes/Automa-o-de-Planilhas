import openpyxl

print('Bem-vindo ao gerador de planilhas!')
print('Para começar, vamos criar uma nova página dentro de uma planilha.')

workbook = openpyxl.Workbook()
del workbook['Sheet']

while True:
    new_sheet_name = input('Digite o nome da página: ')
    workbook.create_sheet(new_sheet_name)

    add_another_sheet = input('Criar mais uma página nesta planilha?(s/n): ')
    if add_another_sheet == 'n': break


sheet_choice = input("Digite o nome da página a ser manipulada: ")
current_sheet = workbook[sheet_choice]

new_fields = []
while True:
    new_field = input('Digite um nome de uma coluna para o cabeçalho: ')
    new_fields.append(new_field)


    add_new_field = input('Adicionar mais uma coluna?(s/n): ')
    if add_new_field == 'n': break

current_sheet.append(new_fields)

# Apenas para teste da planilha
workbook.save('dados.xlsx')