import PySimpleGUI as sg 


class AddSheet():
        
        sg.theme('DarkGreen5') 

        layout_descricao = [
            [sg.Text('Bem-vindo ao gerador de planilhas!')],
            [sg.Text('Para começar, vamos criar uma nova página dentro de uma planilha.')],
        ]

        layout_dados_entrada = [
            [sg.Text('Digite o nome da página:')],
            [sg.Input(key='sheet', size=(26,1))],
            [sg.Button('Adicionar',size=(10,1)), sg.Button('Limpar', size=(10,1))],
            [sg.Button('Continuar', size=(22,1))]
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
    


class SelectPage():
    
    def retorna_layout_principal(sheets):
        sg.theme('DarkGreen5') 

        layout_principal = [
            [sg.Text('Selecione o nome da página a ser manipulada:')]
        ]

        sheet_options = []
        for sheet in sheets:
            sheet_options.append(
                sg.Radio(sheet, group_id='sheet_selection', key=f'{sheet}'))

        layout_principal.append(sheet_options)
        layout_principal.append([sg.Button('Continuar')])
        return layout_principal


window = sg.Window('Teste', layout=SelectPage.retorna_layout_principal(['camisas','sapatos','tesouras']))
window.read()