def difference_of_sums(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    # num1: sum(numbers) NOT divisible by m
    # num2: sum(numbers) divisible by m
    num1 = 0
    num2 = 0
    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i

    return num1 - num2


if __name__ == "__main__":
    n = 10
    m = 3
    print(difference_of_sums(n, m))