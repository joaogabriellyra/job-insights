from src.pre_built.counter import count_ocurrences


def test_counter():
    'Para a palavra javascript a função deve retornar o número 122'
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
