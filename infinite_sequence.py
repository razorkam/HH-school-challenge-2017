
""" computes position of positive int (not arbitrary sequence) in infinite sequence"""


# number - positive int
def compute_position(number):
    prev = number - 1
    d = len(str(prev))  # digits in previous number
    pos = (prev - 10 ** (d - 1) + 1) * d
    for i in range(1, d):
        pos += 9 * 10 ** (i - 1) * i

    return pos + 1


"""finds sequence position in infinite sequence"""


# sequence - int
def find_sequence(sequence):  # sequence can't start from 0 as 'sequence' parameter is int
    str_s = str(sequence)
    n = len(str_s)
    for i in range(1, n + 1):  # test ints with number of digits(i) in [1;n]
        i_pow = 10 ** i
        min_start = i_pow
        start_digit = 0
        for j in range(0, i):  # test if sequence starts from j'th digit of i-digit number
            test_str = str_s[0:i - j]
            start_num = int(test_str)
            if j == 0:
                second_num = start_num + 1
            else:
                i_j_pow = 10 ** (i - j)
                second_num = int(str_s[i - j:i]) * i_j_pow + (start_num + 1) % i_j_pow
                if second_num == 0:
                    continue
            next_num = second_num

            while len(test_str) < n and test_str == str_s[:len(test_str)]:
                test_str += str(next_num)
                next_num += 1

            if test_str[0:n] == str_s and second_num - 1 < min_start:
                min_start = second_num - 1
                start_digit = j

        if min_start != i_pow:  # if min was changed at least once, i.e. sequence was found
            offset = 0
            if start_digit != 0:
                offset = i - start_digit
                min_start += 1
            return compute_position(min_start) - offset

    return 0  # error: sequence not found


if __name__ == '__main__':
    k = 111
    print(k, find_sequence(k))
