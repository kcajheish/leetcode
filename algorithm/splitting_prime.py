from math import sqrt
def splittingPrime(s):
    results = []
    backtrack(s, 0, [], results)
    return results

def prime(n):
    n = int(n)
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def prime_recursive(n, i):
    if n ==0 or n ==1:
        return False

    if n == i:
        return True

    if n % i == 0:
        return False

    return prime_recursive(n, i+1)

def backtrack(s, start, subset, results):
    if start == len(s):
        results.append(list(subset))
        return

    for end in range(start,len(s)):
        split = s[start:end+1]
        is_prime = prime(split)
        if not is_prime:
            continue
        else:
            subset.append(split)
            backtrack(s, end+1, subset, results)
            subset.pop()

r = splittingPrime("1173")
print(r)