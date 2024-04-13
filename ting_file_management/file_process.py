import sys
from ting_file_management.file_management import txt_importer  # type: ignore
from ting_file_management.queue import Queue  # type: ignore


def process(path_file, instance: Queue):  # type: ignore
    name = txt_importer(path_file)  # type: ignore
    if name is None:  # type: ignore
        return None

    file_in_queue = any(data["nome_do_arquivo"] == path_file  # type: ignore
                        for data in instance)  # type: ignore

    if not file_in_queue:  # type: ignore
        data = {  # type: ignore
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(name),  # type: ignore
            "linhas_do_arquivo": name,
        }
        print(data, file=sys.stdout)  # type: ignore
        instance.enqueue(data)  # type: ignore


def remove(instance: Queue):
    if instance.__len__() == 0:  # type: ignore
        print("Não há elementos", file=sys.stdout)
    else:
        removed = instance.dequeue()['nome_do_arquivo']  # type: ignore
        print(f"Arquivo {removed} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):  # type: ignore
    try:
        data = instance.search(position)  # type: ignore
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
