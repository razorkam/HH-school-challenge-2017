from is_kmp import wrap


""" computes position of number(not sequence) in infinite sequence"""

def compute_position(number):  # number is positive int
    prev = number - 1
    d = len(str(prev))  # digits in previous number
    pos = (prev - 10 ** (d - 1) + 1) * d
    for i in range(1, d):
        pos += 9 * 10 ** (i - 1) * i

    return pos + 1


# sequence - int
def find_sequence(sequence):
    str_s = str(sequence)
    n = len(str_s)
    for i in range(1, n+1):  # test ints with number of digits(i) in [1;n]
        min_start = 10**i
        start_digit = 0
        for j in range(0, i):  # test if sequence starts from j'th digit of i-digit number
            test_str = str_s[0:i-j]
            start_num = int(test_str)
            if j == 0:
                second_num = start_num + 1
            else:
                second_num = int(str_s[i-j:i]) * 10**(i-j) + (start_num + 1) % 10**(i-j)
                if second_num == 0:
                    continue
            next_num = second_num
            while len(test_str) < n and test_str == str_s[:len(test_str)]:
                    test_str += str(next_num)
                    next_num += 1

            if test_str[0:n] == str_s and second_num - 1 < min_start:
                min_start = second_num - 1
                start_digit = j


        if min_start != 10**i:  # was changed
            shift = 0
            if start_digit != 0:
                shift = i - start_digit
                min_start += 1
            return compute_position(min_start) - shift




if __name__ == '__main__':
    # mismatches = 0
    # for k in range(13454657647352344, 13454657647352345):
    #     my = find_sequence(k)
    #     true = wrap(str(k))
    #     # true = 1
    #     # if k % 100 == 0:
    #     #     print("step ", k)
    #     if my != true:
    #          # print("Failed!")
    #         # print("My: ", my, " true: ", true)
    #          mismatches += 1
    # print("mismatches", mismatches)

    k = 11111111111111111111111111111111111111111111111111
    print(k, find_sequence(k))