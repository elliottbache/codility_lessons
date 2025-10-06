from Flags import flags_solution

def test_flags_solution():

    assert flags_solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    assert flags_solution([1, 3, 2]) == 1
    assert flags_solution([3, 2, 1]) == 0
