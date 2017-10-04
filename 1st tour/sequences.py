# TODO: compute wonderfule numbers amount in range [left,right], where number is magic when all of it's
# digits are included in one of sums (or more) equal 10 (adding digits to sum sequantially)


def is_wonderful(num):
    lst = [int(i) for i in str(num) if i != '0']
    flags = [False] * len(lst)
    for i, digit in enumerate(lst):
        wnd_sum = digit
        j = i + 1
        while j < len(lst):
            wnd_sum += lst[j]
            if wnd_sum == 10:
                flags[i:j+1] = [True] * (j-i+1)
                break
            elif wnd_sum > 10:
                break

            j += 1

    return all(flag is True for flag in flags)


def solution(left, right):
    wnd_numbers = 0
    for num in range(left, right + 1):
        if is_wonderful(num):
            wnd_numbers += 1

    return wnd_numbers

if __name__ == "__main__":
    left = input("Left border?")
    right = input("Right border?")
    print("Wonderfule numbers: ", solution(int(left), int(right)))