import sys


def txt_importer(path_file: str):
    txt_stderr = sys.stderr
    if path_file.split('.')[-1] != 'txt':
        txt_stderr.write('Formato inválido')
    try:
        with open(path_file) as file:
            content = file.read()
            return content.split('\n')
    except FileNotFoundError:
        txt_stderr.write(f'Arquivo {path_file} não encontrado\n')
