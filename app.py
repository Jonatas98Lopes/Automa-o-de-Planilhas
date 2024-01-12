import openpyxl

print('Bem-vindo ao gerador de planilhas!')
print('Para começar, vamos criar uma nova página dentro de uma planilha.')

workbook = openpyxl.Workbook()
del workbook['Sheet']