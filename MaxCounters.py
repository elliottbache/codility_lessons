"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

A[0] = 3 A[1] = 4 A[2] = 4 A[3] = 6 A[4] = 1 A[5] = 4 A[6] = 4
content_copy
the values of the counters after each consecutive operation will be:

(0, 0, 1, 0, 0) (0, 0, 1, 1, 0) (0, 0, 1, 2, 0) (2, 2, 2, 2, 2) (3, 2, 2, 2, 2) (3, 2, 2, 3, 2) (3, 2, 2, 4, 2)
content_copy
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }
content_copy

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

A[0] = 3 A[1] = 4 A[2] = 4 A[3] = 6 A[4] = 1 A[5] = 4 A[6] = 4
content_copy
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1
content_copy
].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    """
    from itertools import groupby
    from collections import Counter

    max_counter = 0
    while A:
#        print("A = ", A)
        if N+1 in A:
            idx_reset = A.index(N+1)
        else:
            break
#        print("idx_reset", idx_reset)

        # Create slice up to index
        B = A[:idx_reset]
#        print("B = ",B)

        if B:
            counts = Counter(B)  # count occurrences
            most_common_elem, freq = counts.most_common(1)[0]  # top 1

            # Add max occurrences
            max_counter += freq

        # Slice A to remove first part
        if idx_reset < len(A) - 1:
            A = A[idx_reset+1:]
        else:
            break


#    print("max_counter = ",max_counter)

    counters = [max_counter] * N
#    print("counters = ",counters)

    # Repeat for remaining elements
    if A:
        if A[0] < N+1:
            for idx in A:
#                print("A = ",A)
#                print("idx = ",idx)
                counters[idx-1] += 1

    """

    """
    # indices of max_counter reset
    indices = [index for index, value in enumerate(A) if value == N+1]
    print("indices = ",indices)

    # Loop through indices
    max_counter = 0
    for idx in indices:

        # Create slice up to index
        B = A[:idx]

        # Find max occurrences
        temp = groupby(B)
        res = max(temp, key=lambda sub: len(list(sub[1])))

        # Add max occurrences
        max_counter += res[0]

        # Slice A to remove first part
        A = A[idx:]
    """

    counters = [0] * N

    print(f"A = {A}")
    # Loop through A
    for x in A:

        print("x = ",x)

        # If A[K] <= N then increment K
        if x <= N:
            print("counters[x] = ",counters[x-1])
            counters[x-1] = counters[x-1] + 1

        # else set all counters to max_counter
        else:
            counters = [max(counters)] * N

    return counters

if __name__ == "__main__":

    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))
    print(solution(1, [2, 1, 1, 2, 1]))
    print(solution(5, [6, 6, 6, 6, 6, 6]))