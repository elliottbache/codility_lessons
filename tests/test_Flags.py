import pytest

from Flags import flags_solution

@pytest.fixture
def base_case():
    return [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

@pytest.fixture
def simple_input_one_peak():
    return [1, 3, 2]

@pytest.fixture
def simple_input_no_peaks():
    return [3, 2, 1]

def test_base_case(base_case):

    assert flags_solution(base_case) == 3

def test_simple_input(simple_input_one_peak,simple_input_no_peaks):

    assert flags_solution(simple_input_one_peak) == 1
    assert flags_solution(simple_input_no_peaks) == 0