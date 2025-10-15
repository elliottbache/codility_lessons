import pytest
from chocolates_by_numbers import chocolates_by_numbers_solution

@pytest.fixture
def N():
    return 10

@pytest.fixture
def M():
    return 4

def test_chocolates_by_numbers_solution(N, M):
    assert chocolates_by_numbers_solution(N, M) == 5
