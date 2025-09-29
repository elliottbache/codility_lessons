"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

content_copy
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)
content_copy

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

content_copy
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    counter = 0
    last_value = 0.5

    # loop through A
    for current_value in A:

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

    # reset counter and initialize index
    counter = 0

    # loop through A
    for i in range(len(A)):

        # if last value = current value, increment counter and save index
        if last_value == A[i]:

            counter += 1
            idx = i

    # if counter > len(A)/2, return index
    if counter > len(A)/2:

        return idx

    else:

        return -1


if __name__ == '__main__':
    assert solution([3, 4, 3, 2, 3, -1, 3, 3]) in [0, 2, 4, 6, 7]