import openpyxl
from interface import *



workbook = openpyxl.Workbook()
del workbook['Sheet']

new_sheets = []
new_columns = []


adiciona_sheets_planilha_, escolhe_sheet_ = adiciona_sheets_planilha(), None
adiciona_colunas_ = None

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED: break

    if window == adiciona_sheets_planilha_:

        if event == 'Adicionar':
            if values['sheet'] != '':
                window['Continuar'].update(disabled=False)
                print(values['sheet'])
                new_sheets.append(values['sheet'])
                window['sheet'].update('')

        elif event == 'Limpar':
            window['sheet'].update('')

        elif event == 'Continuar':
            for new_sheet in new_sheets:
                workbook.create_sheet(new_sheet)
            adiciona_sheets_planilha_.close()
            escolhe_sheet_ = escolhe_sheet(workbook.sheetnames)
            

    elif window == escolhe_sheet_:
        for key, value in values.items():
            if value:
                name_current_sheet = key
                current_sheet = workbook[key]
        escolhe_sheet_.close()
        adiciona_colunas_ = adiciona_colunas(name_current_sheet)

    elif window == adiciona_colunas_:

        if event == 'Adicionar':
            if values['column_name'] != '':
                window['Continuar'].update(disabled=False)
                print(values['column_name'])
                new_columns.append(values['column_name'])
                window['column_name'].update('')

        elif event == 'Limpar':
                window['column_name'].update('')
        
        elif event == 'Continuar':
            pass



""" sheet_choice = input("Digite o nome da página a ser manipulada: ")
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
 """