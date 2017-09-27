# TODO: let function s(n) returns less number m , so that m! is divided by n.
# compute sum of all s(n) for n in [left, right]

def er_sieve(n):  # computes all prime numbers up to n
    is_prime = [True] * (n+1)  # 0..n , initially assume all are primes
    is_prime[0:2] = [False] * 2  # 0 and 1 are not primes
    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n+1, p):
                is_prime[i] = False
        p += 1

    return list(i for i, p in enumerate(is_prime) if p)


def factorize(n, primes_list):
    factors = []
    gen = primes_list
    for pr_num in gen:
        if pr_num**2 > n:
            break
        while n % pr_num == 0:
            n //= pr_num
            factors.append(pr_num)
    if n > 1:
        factors.append(n)
    return factors


def s_function(n, primes_list):
    factors = factorize(n, primes_list)
    num = factors[0]
    pr_groups = {num: 1}
    for f in factors[1:]:  # get dict
        if f == num:
            pr_groups[num] += 1
        else:
            num = f
            pr_groups[num] = 1

    min_factorials = []
    for prime, appeared in pr_groups.items():
        if appeared == 1 or prime*appeared < max(pr_groups.keys()):
            min_factorials.append(prime)
        else:
            cur_fact = prime
            fact_to_add = cur_fact
            collected = 1
            while collected < appeared:
                cur_fact = fact_to_add + prime
                fact_to_add = cur_fact
                while cur_fact % prime == 0:
                    cur_fact //= prime
                    collected += 1
            min_factorials.append(fact_to_add)
    # print(n, factors)
    return max(min_factorials)


def solution(l, r, primes_list):
    total_sum = 0
    for n in range(l, r+1):
        s = s_function(n, primes_list)
        #print("N=" , n, "S=", s)
        total_sum += s


    return total_sum


if __name__ == "__main__":
    left = int(input("Left"))
    right = int(input("Right"))
    pr_list = er_sieve(right)
    print("Er sieve OK")
    print(solution(left, right, pr_list))
