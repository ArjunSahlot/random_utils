def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def find_factors(num):
    factors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            if i not in factors:
                factors.append(i)
            if num//i not in factors:
                factors.append(num//i)

    return factors
