def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Create a list to mark prime numbers
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if primes[p] == True:
            # Update all multiples of p to False (not prime)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if primes[p]:
            print(p)

# Input: Get prime n
# Input: Get prime numbers up to n
n = int(input("Enter a number: "))
sieve_of_eratosthenes(n)