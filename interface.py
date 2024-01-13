import PySimpleGUI as sg 
import openpyxl


def adiciona_sheets_planilha() -> sg.Window:
    sg.theme('DarkGreen5') 

    layout_descricao = [
        [sg.Text('Bem-vindo ao gerador de planilhas!')],
        [sg.Text('Para começar, vamos criar uma nova página dentro de uma planilha.')],
    ]

    layout_dados_entrada = [
        [sg.Text('Digite o nome da página:')],
        [sg.Input(key='sheet', size=(26,1))],
        [sg.Button('Adicionar',size=(10,1)), sg.Button('Limpar', size=(10,1))],
        [sg.Button('Continuar', size=(22,1), disabled=True)]
    ]

    layout_saida = [
        [sg.Text()],
        [sg.Output(size=(50,5))]
    ]

    layout_principal = [
        [sg.Column(layout_descricao)],
        [
            sg.Column(layout_dados_entrada), 
            sg.Column(layout_saida), 
        ]
    ]
    return sg.Window('Adicione a(s) página(s) na planilha:', 
        layout=layout_principal, finalize=True)



    
def escolhe_sheet(sheets) -> sg.Window:
    sg.theme('DarkGreen5') 

    layout_principal = [
        [sg.Text('Selecione o nome da página a ser manipulada:')]
    ]

    sheet_options = []
    for index, sheet in enumerate(sheets):
        if index == 0:
            sheet_options.append(
                sg.Radio(sheet, group_id='sheet_selection', default=True, key=f'{sheet}'))
        else:
            sheet_options.append(
                sg.Radio(sheet, group_id='sheet_selection', key=f'{sheet}'))

    layout_principal.append(sheet_options)
    layout_principal.append([sg.Button('Continuar')])
    return sg.Window('Escolha a página da planilha', layout=layout_principal, finalize=True)


def adiciona_colunas(sheet) -> sg.Window:
    sg.theme('DarkGreen5') 

    layout_dados_entrada = [
        [sg.Text(f'Digite o nome para uma coluna no cabeçalho da página: {sheet}')],
        [sg.Input(key='column_name', size=(26,1))],
        [sg.Button('Adicionar',size=(10,1)), sg.Button('Limpar', size=(10,1))],
        [sg.Button('Continuar', size=(22,1), disabled=True)]
    ]

    layout_saida = [
        [sg.Text()],
        [sg.Output(size=(50,5))]
    ]

    layout_principal = [
        [
            sg.Column(layout_dados_entrada), 
            sg.Column(layout_saida), 
        ]
    ]
    return sg.Window('Adicione a(s) coluna(s) na página:', 
        layout=layout_principal, finalize=True)


def escolher_adicionar_dados() -> sg.Window:
    sg.theme('DarkGreen5') 

    layout = [
        [sg.Text('Adicionar dados a essa planilha?')],
        [
            sg.Radio('Sim', group_id='insert_data', default=True, key='sim'),
            sg.Radio('Não', group_id='insert_data', key='nao'),
        ],
        [sg.Button('Continuar')]
    ]

    return sg.Window('Adicionar dados?', layout=layout, finalize=True)


def salvar_arquivo() -> sg.Window:
    sg.theme('DarkGreen5') 
    
    layout = [
        [sg.Text('Digite o nome da planilha a ser salva:')],
        [
            sg.Input(key='file_name', size=(26,1),), 
            sg.Input('.xlsx', disabled=True, size=(5,1), key='extension')
        ],
        [sg.Text(key='warning_file_name', text_color='white')],
        [
            sg.Button('Salvar', size=(7,1)), 
            sg.Button('Finalizar', disabled=True, size=(10,1))
        ]

    ]

    return sg.Window('Salvar arquivo de planilha:', layout=layout, finalize=True)


def escolher_pagina_adicionar_dados(sheets: list) -> sg.Window:
    sg.theme('DarkGreen5') 

    layout = [
        [sg.Text('Em qual página devemos adicionar dados?')]
    ]

    radio_buttons = []
    for index, sheet in enumerate(sheets):
        if index == 0:
            radio_buttons.append(sg.Radio(
                sheet, default=True, group_id='sheet_choice', key=f"{sheet}"))
        else:
            radio_buttons.append(sg.Radio(
                sheet, group_id='sheet_choice', key=f"{sheet}"))
            
    layout.append(radio_buttons)
    layout.append([sg.Text(key='no_heading', text_color='white'), sg.Button('Continuar')])
            
    return sg.Window('Escolher página:', layout=layout, finalize=True)


def insere_dados_sheet():
    sg.theme('DarkGreen5') 

    layout_dados_entrada = [
        [sg.Text('Digite APENAS um dado por vez abaixo:')],
        [
            sg.Input(key='data', size=(28,1)),
            sg.Text('Adicione a linha de dados clicando abaixo:',)
        ],
        [
            sg.Button('Adicionar dado',size=(12,1)), 
            sg.Button('Limpar', size=(10,1)),
            sg.Button('Enviar linha',  size=(30,1))
        ],
        [sg.Button('Continuar', size=(24,1), disabled=True)]
    
    ]
    layout_saida = [
        [sg.Text()],
        [sg.Output(size=(40,5))]
    ]

    layout_principal = [
        [
            sg.Column(layout_dados_entrada), 
            sg.Column(layout_saida), 
        ]
    ]
    
    return sg.Window('Adicione dados à página:', layout=layout_principal, finalize=True)


