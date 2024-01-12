import openpyxl
from interface import *



workbook = openpyxl.Workbook()
del workbook['Sheet']

window = sg.Window('Teste', layout=AddSheet.layout_principal)
new_sheets = []

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED: break

    elif event == 'Adicionar':
        new_sheets.append(values['sheet'])
        print(values['sheet'])
        window['sheet'].update('')

    elif event == 'Limpar':
        window['sheet'].update('')

    elif event == 'Continuar':
        pass

    #new_sheet_name = input('Digite o nome da página: ')
    #workbook.create_sheet(new_sheet_name)

    #add_another_sheet = input('Criar mais uma página nesta planilha?(s/n): ')
    #if add_another_sheet == 'n': break


sheet_choice = input("Digite o nome da página a ser manipulada: ")
current_sheet = workbook[sheet_choice]

new_fields = []
while True:
    new_field = input('Digite um nome de uma coluna para o cabeçalho: ')
    new_fields.append(new_field)


    add_new_field = input('Adicionar mais uma coluna?(s/n): ')
    if add_new_field == 'n': break

current_sheet.append(new_fields)

add_data_in_sheet = input("Adicionar dados a essa planilha?(s/n): ")
if add_data_in_sheet == 's':

    available_sheets = workbook.sheetnames
    print(f'As páginas disponíveis são: {available_sheets}')

    sheet_choice = input("Em qual página devemos adicionar dados? ")
    current_sheet = workbook[sheet_choice]

    while True:
        data = input("Digite os dados a serem adicionados a uma nova linha, separadas por vírgula: ").strip()
        current_sheet.append(data.split(','))

        add_new_data_line = input("Adicionar uma nova linha?(s/n): ")
        if add_new_data_line == 'n': break
    
workbook_name = input("Digite o nome da planilha a ser salva: ").strip()
workbook.save(f'{workbook_name}.xlsx')
print("Planilha criada com sucesso.")



