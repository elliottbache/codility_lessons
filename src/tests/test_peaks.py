import pytest
from peaks import peaks_solution

@pytest.fixture
def A():
    return [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

def test_peaks_solution(A):
    assert peaks_solution(A) == 3
