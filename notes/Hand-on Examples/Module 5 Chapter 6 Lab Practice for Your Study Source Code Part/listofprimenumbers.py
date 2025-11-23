# List of Prime Numbers Up to n
# Write a function prime_numbers(n) that returns a list of prime numbers up to n.
def prime_numbers(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for div in range(2, int(num**0.5) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

"""
Example usage:
prime_numbers(7)
"""
