"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

content_copy
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)
content_copy

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

content_copy
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].
"""

from typing import List


def count_semiprimes_solution(N: int, P: List[int], Q: List[int]) -> List[int]:
    """Calculate number of semiprimes within each range.

    Given 2 lists with ranges, return a list of the number of
    semiprimes in these ranges.

    Args:
        N (int): the maximum semiprime
        P (List[int]): the list of range start
        Q (List[int]): the list of range end

    Returns:
        List[int]: the number of semiprimes within each range

    Usage:
    >>> count_semiprimes_solution(26, [1, 4, 16], [26, 10, 20])
    [10, 4, 0]
    """
    # create list of prime numbers up to sqrt(N)
    primes = sieve(N//2)

    # create list of semiprimes
    semiprimes = set()
    for i in range(len(primes)):
        prime_slice = primes[i:]
        for prime2 in prime_slice:
            semiprime_candidate = primes[i]*prime2
            if semiprime_candidate <= N:
                semiprimes.add(semiprime_candidate)
    semiprimes = sorted(semiprimes)

    # create list with number of semiprimes at current index
    semiprime_count = [0] * (N+1)
    j = 0
    for i in range(1,len(semiprime_count)):
        if j < len(semiprimes) and i == semiprimes[j]:
            semiprime_count[i] = semiprime_count[i-1] + 1
            j += 1
        else:
            semiprime_count[i] = semiprime_count[i-1]

    # loop through P and Q
    results = list()
    for i in range(len(P)):

        idx = max(P[i] - 1,0)
        results.append(semiprime_count[Q[i]]-semiprime_count[idx])

    return results

def sieve(n):
    """Create list of prime numbers from 1 to n.

    Args:
        n (int): an integer

    Returns:
        list: a list of prime numbers

    Usage:
    >>> sieve(13)
    [2, 3, 5, 7, 11, 13]
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    if len(sieve) > 1:
        sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1

    primes = list()
    for k in range(n+1):
        if sieve[k]:
            primes.append(k)

    return primes

if __name__ == '__main__':
    N = 26
    P = [1, 4, 16]
    Q = [26, 10, 20]
    print(solution(N,P,Q))
    print(solution(1, [1], [1]))