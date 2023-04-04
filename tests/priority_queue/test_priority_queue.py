import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    prio_item = {
        "nome_do_arquivo": 'teste/meu_teste.txt',
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['Primeira linha', 'Segunda', 'Terceira'],
    }

    reg_item = {
        "nome_do_arquivo": 'teste/meu_teste.txt',
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            'Primeira linha', 'Segunda', 'Terceira', 'Quarta', 'Quinta'
        ],
    }
    priority_queue = PriorityQueue()
    priority_queue.enqueue(prio_item)
    assert len(priority_queue.regular_priority) == 0
    assert len(priority_queue.high_priority) == 1

    priority_queue.enqueue(reg_item)
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 1

    priority_queue.enqueue(prio_item)
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 2

    priority_queue.enqueue(reg_item)
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue.high_priority) == 2

    first_prio = priority_queue.search(0)
    assert first_prio['qtd_linhas'] == 3

    first_reg = priority_queue.search(3)
    assert first_reg['qtd_linhas'] == 5

    priority_queue.dequeue()
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue.high_priority) == 1

    priority_queue.dequeue()
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue.high_priority) == 0

    priority_queue.dequeue()
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(99)
