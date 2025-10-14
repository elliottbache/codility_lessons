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

    from collections import defaultdict

    block_counters = defaultdict(int)
    block_max = 0
    max_counter = 0
    # loop through A
    for x in A:

        # if x = N + 1
        if x == N+1:

            # record max_counter
            max_counter += block_max

            # reset block_max to 0
            block_max = 0

            # clear counters
            block_counters.clear()

        # else
        else:

            # add to counters
            block_counters[x] += 1

            # if counters greater than block_max, increment block_max
            if block_counters[x] > block_max:
                block_max = block_counters[x]

#    print(f"block_counters = {block_counters}")
    # return counters
    counters = [max_counter] * N
    for idx in range(N):
        if idx+1 in block_counters:
            counters[idx] += block_counters[idx+1]

    return counters

if __name__ == "__main__":

    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print("solution = ",solution(N, A))
    print("solution = ",solution(1, [2, 1, 1, 2, 1]))
    print("solution = ",solution(5, [6, 6, 6, 6, 6, 6]))