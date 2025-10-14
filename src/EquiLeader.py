"""A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

content_copy
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

content_copy
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000]."""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):

    equileaders = 0

    # create array for prefixes
    predominators = dominators(A)

    # create array for suffixes
    B = A.copy()
    B.reverse()
    postdominators = dominators(B)
    postdominators.reverse()

    # loop through A
    for i in range(0, len(A) - 1):

        # if leaders are equal
        if predominators[i] == postdominators[i+1] and predominators[i] != 1000000001:

            # add to counter
            equileaders += 1

    return equileaders

def dominators(A):
    counter = 0
    last_value = 0.5
    predominators = list()
    counters = defaultdict(int)

    # loop through A
    for i in range(len(A)):

        current_value = A[i]

        # if counter > 0
        if counter > 0:

            # compare current value to last value
            if current_value == last_value:

                counter += 1

            # else decrement counter
            else:
                counter -= 1

        # else counter = 1 and last value is current value
        else:

            counter = 1
            last_value = current_value

        # add to dict to count occurrences of current_value
        counters[current_value] += 1

        # if we have a dominant value, append to list
        if counter > 0 and counters[last_value] > (i+1)/2:

            predominators.append(last_value)

        # else append dummy value out of range
        else:

            predominators.append(1000000001)

    return predominators

if __name__ == '__main__':
    assert solution([4, 3, 4, 4, 4, 2]) == 2
    assert solution([1, 2, 3, 4, 5]) == 0
    print(solution([1, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 1]))