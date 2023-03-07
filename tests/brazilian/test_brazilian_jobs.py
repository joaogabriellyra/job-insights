from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    'as chaves do dict salário, título e tipo devem retornar em inglês'
    headers, *content = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert "title" and "salary" and "type" in headers
