
import itertools

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


def equal_ignore_order(a, b):
    unmatched = list(b)
    for element in a:
        try:
            unmatched.remove(element)
        except ValueError:
            return False
    return not unmatched


def split(lst, splits):
    splits += "0"
    output = [[]]
    for index, item in enumerate(lst):
        output[-1].append(item)
        if splits[index] == "1":
            output.append([])
    return output


def partition(nums):  # this could be more efficient
    partitions = []
    partitions.append([nums])
    permutations = list(itertools.permutations(nums))
    for perm in permutations:
        for i in range(2**(len(nums)-1)-1):
            splits = bin(i+1)
            splits = str(splits)[2:]
            while len(splits) < len(nums)-1:
                splits = "0"+splits
            
            partitions.append(split(perm, splits))
    

    for i, partition in enumerate(partitions):
        for j, subset in enumerate(partition):
            partition[j] = sorted(subset)
        partitions[i] = partition



    unique_partitions = []
    already_seen = False
    for i in partitions:
        for j in unique_partitions:
            if equal_ignore_order(i, j):
                already_seen = True
        if not already_seen:
            unique_partitions.append(i)
        already_seen = False

    return unique_partitions
