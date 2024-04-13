import sys


def txt_importer(path_file):  # type: ignore
    if not path_file.endswith(".txt"):  # type: ignore
        print("Formato inválido", file=sys.stderr)  # type: ignore
        return []  # type: ignore

    try:
        with open(path_file, "r") as file:  # type: ignore
            return file.read().split("\n")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []  # type: ignore
