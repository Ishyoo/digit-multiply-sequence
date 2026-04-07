
def isprime(num):
    for i in range(2, int((num**0.5))+1):
        if num % i == 0:
            return False
    return True


def factors(num):
    factors = []
    for i in range(1, int((num**0.5))+1):
        if num % i == 0:
            factors.append((i, num//i))
    return factors


def prime_factors(num):
    solution = []
    if isprime(num):
        return [num]

    for factor in factors(num)[-1]:
        if not isprime(factor):
            for i in prime_factors(factor):
                solution.append(i)
        else:
            solution.append(factor)

    return solution
