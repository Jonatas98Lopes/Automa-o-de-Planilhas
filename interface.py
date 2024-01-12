import PySimpleGUI as sg 




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

#window = sg.Window('Teste', layout=SelectPage.retorna_layout_principal(['camisas','sapatos','tesouras']))
#window.read()