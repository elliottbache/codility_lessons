import pytest
from count_semiprimes import count_semiprimes_solution

@pytest.mark.parametrize("N, P, Q, expected",[
    (26, [1, 4, 16], [26, 10, 20], [10, 4, 0]),
    (1, [1], [1], [0])
])

def test_count_semiprimes_solution(N, P, Q, expected):
    assert count_semiprimes_solution(N, P, Q) == expected
