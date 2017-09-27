#TODO find less positive integer x, so that 3*x and 6*x are equal up to digits permutation


def solution():
    number = 3
    while True:
        if (number % 9) == (number * 2) % 9:  # digits sums are equal
        if ''.join(sorted(str(number))) == ''.join(sorted(str(number*2))):
            return number // 3
        number += 3

if __name__ == "__main__":
    print(solution())