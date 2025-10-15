import pytest

from flags import flags_solution

@pytest.mark.parametrize("A, expected", [
    ([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3),
    ([1, 3, 2], 1),
    ([3, 2, 1], 0)
])
def test_flags_solution(A, expected):
    assert flags_solution(A) == expected