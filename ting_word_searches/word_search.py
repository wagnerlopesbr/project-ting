from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):  # type: ignore
    results = []

    for file_data in instance:  # type: ignore
        occurrences = []
        file_name = file_data["nome_do_arquivo"]  # type: ignore
        lines = file_data["linhas_do_arquivo"]  # type: ignore

        for i, line in enumerate(lines, 1):  # type: ignore
            if word.lower() in line.lower():  # type: ignore
                occurrences.append({"linha": i})  # type: ignore

        if occurrences:
            results.append({  # type: ignore
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results  # type: ignore


def search_by_word(word, instance):  # type: ignore
    """Aqui irá sua implementação"""
