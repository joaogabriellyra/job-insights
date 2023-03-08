from src.pre_built.sorting import sort_by
from src.insights.jobs import read
import pytest


def test_sort_by_criteria():
    with pytest.raises(ValueError, match="invalid sorting criteria"):
        sort_by(read("data/jobs.csv"), "max_salari")
