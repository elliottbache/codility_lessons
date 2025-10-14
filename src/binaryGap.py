def convert_to_binary(n):
    res = ''  # binary result

    while n > 0:
        res = str(n & 1) + res
        n >>= 1

    return res

#def count_zeroes(b):

def solution(N):
    # convert from decimal to binary
    b = convert_to_binary(N)

    length = 0
    max_length = length
    is_first = False

    # loop through binary
    for i in range(len(b)):

        # if  a 0 is found, add to length
        if b[i] == '0' and is_first:
            length += 1

        # if a 1 is found, restart counter
        if b[i] == '1':

            is_first = True

            # if length is longer than max_length, save as max_length
            if length > max_length:
                max_length = length

            length = 0

    return max_length

if __name__ == "__main__":

    print(solution(53))