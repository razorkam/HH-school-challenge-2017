#  TODO: compute syx + yur = rrsy solutions, where digits are switched by letters. Leading zeros are not allowed
#  == 90s + 109y + x + 10u - 1099r = 0

def solution():  # brute
    x_range = range(0, 10)
    y_range = range(1, 10)
    r_range = range(1, 10)
    s_range = range(1, 10)
    u_range = range(0, 10)

    sols = 0

    for x in x_range:
        for y in y_range:
            for r in r_range:
                for s in s_range:
                    for u in u_range:
                        dupl_check = [s, x, y, u, r]
                        if 90 * s + 109 * y + x + 10 * u - 1099 * r == 0 and \
                                        len(dupl_check) == len(set(dupl_check)):
                            sols += 1
                            print(''.join((str(s), str(y), str(x))), ' + ', ''.join((str(y), str(u), str(r))) +
                                  ' = ' + ''.join((str(r), str(r), str(s), str(y))))

    return sols


if __name__ == "__main__":
    print("Solutions: ", solution())
