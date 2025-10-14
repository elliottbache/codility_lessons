import pytest
from count_non_divisible import count_non_divisible_solution

@pytest.mark.parametrize("A, expected", [
    ([3, 1, 2, 3, 6], [2, 4, 3, 2, 0]),
    ([2], [0])
])

def test_count_non_divisible_solution(A, expected):
    assert count_non_divisible_solution(A) == expected
