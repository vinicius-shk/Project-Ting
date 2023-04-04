import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance.fila:
        if path_file == item['nome_do_arquivo']:
            return None
    process_out = sys.stdout
    content = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }
    instance.enqueue(processed_data)
    print(processed_data, file=process_out)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
