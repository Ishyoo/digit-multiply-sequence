
import factor as factor
import itertools

def children(num):  # generate all partitions of the set
    factors = factor.prime_factors(num)
    partitions = factor.partition(factors)
    products = [[]]
    for partition in partitions:
        for number in partition:
            product = 1
            for fact in number:
                product *= fact
            products[-1].append(product)
        products.append([])
    products = products[:-1]

    print(products)
    for i in products[:]:
        for j in i:
            if len(str(j)) > 1:
                products.remove(i)
    print(products)

    child = ""
    children = []
    for i in products:
        for perm in itertools.permutations(i):
            for char in perm:
                child += str(char)
            children.append(int(child))
            child = ""
    
    return list(set(children))
            




def parent(num):
    result = 1
    for i in str(num):
        result *= int(i)

    return result

print(children(24))
