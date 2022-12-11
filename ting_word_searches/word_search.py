def exists_word(word, instance):

    result = search_by_word(word, instance)

    for dict in result:
        for occurrence in dict['ocorrencias']:
            del occurrence['conteudo']
    return result


def search_by_word(word, instance):
    result = []
    for dict in instance:
        occurrences = []
        for index, line in enumerate(dict['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({
                    'linha': index + 1,
                    'conteudo': line
                })

        if len(occurrences):
            data = {
                'palavra': word,
                'arquivo': dict['nome_do_arquivo'],
                'ocorrencias': occurrences
            }
            result.append(data)
    return result
