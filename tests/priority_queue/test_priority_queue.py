import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    test_q = PriorityQueue()
    test_q.enqueue({"data": "Value 1", "qtd_linhas": 4})
    test_q.enqueue({"data": "Value 2", "qtd_linhas": 7})
    test_q.enqueue({"data": "Value 3", "qtd_linhas": 3})
    test_q.enqueue({"data": "Value 4", "qtd_linhas": 5})
    test_q.enqueue({"data": "Value 5", "qtd_linhas": 1})

    assert len(test_q) == 5

    assert test_q.search(4) == {"data": "Value 4", "qtd_linhas": 5}

    with pytest.raises(IndexError):
        test_q.search(999)

    data_2 = test_q.dequeue()
    data_1 = test_q.dequeue()

    assert data_1 == {"data": "Value 3", "qtd_linhas": 3}
    assert data_2 == {"data": "Value 1", "qtd_linhas": 4}
