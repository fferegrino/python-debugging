def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def permutations(n, k):
    return factorial(n) // factorial(n - k)

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def factorial(n):
    # Base case: when n is 0, factorial is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n)

# Let's try to calculate the factorial of 5
result = factorial(5)
print(f"The factorial of 5 is {result}")