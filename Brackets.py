"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)
content_copy
" or "[U]
content_copy
" or "{U}
content_copy
" where U is a properly nested string;
S has the form "VW
content_copy
" where V and W are properly nested strings.
For example, the string "{[()()]}
content_copy
" is properly nested but "([)()]
content_copy
" is not.

Write a function:

def solution(S)
content_copy

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}
content_copy
", the function should return 1 and given S = "([)()]
content_copy
", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(
content_copy
', '{
content_copy
', '[
content_copy
', ']
content_copy
', '}
content_copy
' and/or ')
content_copy
'.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # initialize stacks to hold symbols
    symbols = list()

    # loop through S
    for char in S:

        # if left symbol, append
        if char == '(':
            symbols.append(1)
        elif char == '[':
            symbols.append(2)
        elif char == '{':
            symbols.append(3)
        # if right symbol, pop
        elif char == ')' or char == ']' or char == '}':

            # if no more items in list, we have extra closing symbol
            if len(symbols) == 0:
                return 0

            if char == ')' and symbols[-1] == 1:
                symbols.pop()
            elif char == ']' and symbols[-1] == 2:
                symbols.pop()
            elif char == '}' and symbols[-1] == 3:
                symbols.pop()
            else:
                return 0

    # if remaining symbol, return 0
    if len(symbols) > 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    assert solution("{[()()]}") == 1
    assert solution("([)()]") == 0

