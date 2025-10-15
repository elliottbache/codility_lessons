"""
Two positive integers N and M are given. Integer N represents the
number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave
only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1
chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat
the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following
chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat,
following the above rules.

Write a function:

def chocolates_by_numbers_solution(N, M)

that, given two positive integers N and M, returns the number of chocolates
that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5,
as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def chocolates_by_numbers_solution(N: int, M: int) -> int:
    """Count number of chocolates in a circle that you eat before
    coming across a wrapper.

    The chocolates are arranged in a circle.  Once eating a chocolate,
    you leave the wrapper.  You continue advancing until reaching a
    wrapper.

    Args:
        N (int): number of chocolates

    Returns:
        int: number of chocolates you skip each time

    Examples:
        >>> from src.chocolates_by_numbers import chocolates_by_numbers_solution
        >>> chocolates_by_numbers_solution(10, 4)
        5
    """

    # find least common multiple
    lcm = least_common_multiple(N, M)

    # divide lcm by M
    return lcm // M


def least_common_multiple(a: int, b: int) -> int:
    """Return the least common multiple of two integers.

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: least common multiple of two integers

    Examples:
        >>> from src.chocolates_by_numbers import least_common_multiple
        >>> least_common_multiple(10, 4)
        20
    """

    return a * b // greatest_common_denominator(a, b, 1)


def greatest_common_denominator(a: int, b: int, res: int) -> int:
    """Find the greatest common denominator.

    This uses the divide and conquer technique.  This algorithm is
    efficient for very large integers.  To calculate the gcd,
    set res=1 in the function call.

    Args:
        a (int): first integer
        b (int): second integer
        res (int): remaining integer

    Returns:
        int: greatest common denominator

    Examples:
        >>> from src.chocolates_by_numbers import greatest_common_denominator
        >>> greatest_common_denominator(10, 4, 1)
        2
    """

    if a == b:
        return res * a
    if a % 2 == 0 and b % 2 == 0:
        return greatest_common_denominator(a // 2, b // 2, 2 * res)
    elif a % 2 == 0:
        return greatest_common_denominator(a // 2, b, res)
    elif b % 2 == 0:
        return greatest_common_denominator(a, b // 2, res)
    elif a > b:
        return greatest_common_denominator(a - b, b, res)
    else:
        return greatest_common_denominator(a, b - a, res)


if __name__ == '__main__':
    print(chocolates_by_numbers_solution(10, 4))
