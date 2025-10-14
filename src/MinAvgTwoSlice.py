"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

content_copy
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

content_copy
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # calclate averages for 2 element slices
    avg_range2 = [10001] * (len(A) - 1)
    for i in range(0,len(avg_range2)):
        avg_range2[i] = (A[i+1] + A[i])/2

    # calclate sums for 3 element slices
    if len(A) > 2:
        avg_range3 = [10001] * (len(A) - 2)
        for i in range(0,len(avg_range3)):
            avg_range3[i] = (A[i+2] + A[i+1] + A[i])/3
    else:
        avg_range3 = [10001]

    # calculate min for 2 element slices
    min2 = min(avg_range2)
    idx_min2 = avg_range2.index(min2)

    # calculate min for 3 element slices
    min3 = min(avg_range3)
    idx_min3 = avg_range3.index(min3)

    # return index of smallest min
    if min2 < min3:
        return idx_min2
    elif min3 < min2:
        return idx_min3
    else:
        return min(idx_min2,idx_min3)

if __name__ == "__main__":
    assert solution([4, 2, 2, 5, 1, 5, 8]) == 1
    assert solution([5, 6, 3, 4, 9]) == 2
