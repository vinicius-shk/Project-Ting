def exists_word(word, instance):
    data = list()
    ocurrencies = list()
    info = {
        "palavra": word,
        "arquivo": '',
        }
    for item in instance.fila:
        info['arquivo'] = item['nome_do_arquivo']
        for idx, line in enumerate(item['linhas_do_arquivo']):
            if word.lower() in line.lower():
                ocurrencies.append({"linha": idx + 1})
        if len(ocurrencies):
            info['ocorrencias'] = [*ocurrencies]
            data.append(info)
            ocurrencies.clear()
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
