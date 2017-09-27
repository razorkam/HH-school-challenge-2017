# 5x5 spiral matrix
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# TODO: compute diagonal elts sum of 1065x1065 spiral matrix

def solution(dimension):
    total_sum = 1  # central elt, layer 0
    layers = (dimension - 1) // 2
    while layers > 0:
        decrement = 2 * layers
        right_up = (decrement + 1) ** 2  # right up element
        layer_sum = 4 * right_up - 6 * decrement
        total_sum += layer_sum
        layers -= 1

    return total_sum


def bruteforce_solution():
    pass


if __name__ == "__main__":
    dimension = int(input("Spiral matrix dimension (odd number)? "))
    print("Diagonal sum: ", solution(dimension))
