"""
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of
elements of the array that are not the divisors of A[i]. We say that these
elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

content_copy
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)
content_copy

that, given an array A consisting of N integers, returns a sequence of integers
representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

content_copy
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N
content_copy
].
"""

from collections import defaultdict
from typing import List, Set, Dict


def count_non_divisible_solution(A: List[int]) -> List[int]:
    """Return list of non-divisors.

    The number of non-divisors for each element is returned as a list
    of integers.

    Args:
        A (list[int]): A list of integers.

    Returns:
        list[int]: The number of non-divisors for each element of A.

    Usage:
    >>> count_non_divisible_solution([3, 1, 2, 3, 6])
    [2, 4, 3, 2, 0]
    >>> count_non_divisible_solution([2])
    [0]
    """

    n_non_divisors = [0] * len(A)
    n = len(A)
    max_element = max(A)

    # create set of possible divisors
    possible_divisors = set(A)

    # create dict of counters for each element of A
    divisor_counters: Dict[int, int] = defaultdict(int)
    for i in A:
        divisor_counters[i] += 1

    # up to max_element do factorization, creating dict of sets
    F = factorization_sets(max_element, possible_divisors)

    n_divisors = dict()
    for divisor in possible_divisors:
        sum = 0
        for element in F[divisor]:
            sum += divisor_counters[element]
        n_divisors[divisor] = sum

    for i in range(len(n_non_divisors)):
        n_non_divisors[i] = n - n_divisors[A[i]]

    return n_non_divisors


def factorization_sets(max_element: int, possible_divisors: Set[int]) \
        -> Dict[int, Set[int]]:
    """Create dict of sets holding factorization for each integer.

    Args:
        max_element (int): The maximum element in the set.
        possible_divisors (set[int]): The set of integers that are also
            possible divisors.

    Returns:
        dict[int, Any]: A dict of sets holding factorization for each integer.

    Usage:
    >>> {k: sorted(v) for k, v in factorization_sets(max_element=6, \
        possible_divisors={1, 2, 3, 6}).items()}
    {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2], 5: [1], 6: [1, 2, 3, 6]}
    """

    F: Dict[int, Set[int]] = dict()
    for i in possible_divisors:
        k = i
        while k <= max_element:
            if k not in F:
                F[k] = set()
            F[k].add(i)
            k += i

    return F


if __name__ == '__main__':

    import doctest

    doctest.testmod()
    A = [3, 1, 2, 3, 6]
    print(count_non_divisible_solution(A))
    A = [2]
    print(count_non_divisible_solution(A))
