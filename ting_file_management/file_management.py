import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r', encoding='utf8') as file:
            content = file.read().splitlines()
            return content
    except IOError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
