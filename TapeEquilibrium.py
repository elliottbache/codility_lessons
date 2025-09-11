"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

A[0] = 3 A[1] = 1 A[2] = 2 A[3] = 4 A[4] = 3
content_copy
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)
content_copy

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

A[0] = 3 A[1] = 1 A[2] = 2 A[3] = 4 A[4] = 3
content_copy
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    min_diff = 10000000000 # very large number that will always be larger than the max diff
    first_sum = 0 # the sum of all of the elements to be later used as sum(B), where A = B.append(C)
    last_sum = sum(A) # the sum of all of the elements to be later used as sum(C), where A = B.append(C)

    # Loop through P (0 < P < N)
    for P in range(1, len(A)):

        first_sum += A[P-1]
        last_sum -= A[P-1]
        abs_diff = abs(first_sum - last_sum)

        # Save if minimum
        if abs_diff < min_diff:
            min_diff = abs_diff

    return min_diff

if __name__ == "__main__":
    A = [3, 1, 2, 4, 3]
    print(solution([3, 1, 2, 4, 3]))
    print(solution([1, 1]))
    print(solution([1212, 1]))
    print(solution([1212, 135556]))