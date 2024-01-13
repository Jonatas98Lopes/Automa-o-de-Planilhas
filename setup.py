import sys
from cx_Freeze import setup, Executable
 
arquivos = [] 

base = "Win32GUI" if sys.platform == "win32" else None
 

configuracao = Executable(
    script='app.py',
    icon='icone.ico', 
    base=base 
)


setup(
    name = 'Gerador de De Planilhas', 
    version = '1.0', 
    description = 'Com esse programa, você pode automatizar o processo de criação de planilhas.',
    author = 'Jonatas L. de Sousa',            
    options = {'build_exe': {'include_files': arquivos,"include_msvcr":True}}, 
    executables = [configuracao]
)