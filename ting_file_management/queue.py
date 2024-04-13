from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = list()  # type: ignore

    def __len__(self):
        return len(self.__data)  # type: ignore

    def enqueue(self, value):  # type: ignore
        self.__data.append(value)  # type: ignore

    def dequeue(self):  # type: ignore
        # i would like to create a deque to use popleft
        # but the requisite asks for a list
        return self.__data.pop(0)  # type: ignore

    def search(self, index):  # type: ignore
        if 0 <= index < len(self.__data):  # type: ignore
            return self.__data[index]  # type: ignore
        raise IndexError("Índice Inválido ou Inexistente")
