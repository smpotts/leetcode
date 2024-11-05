def largest_prime_factor(target):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    divisible = [-1]

    for p in primes:
        remainder = target / p
        # print(remainder)

        if remainder == int(remainder):
            divisible.append(p)

    # print(max(divisible))
    return max(divisible)


if __name__ == "__main__":
    largest_prime_factor(42)