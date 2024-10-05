def minimumOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    operations = 0
    for n in nums:
        if (n + 1) % 3 == 0:
            operations += 1
        else:
            abs_diff = abs(3 - n)
            mod_diff = n % 3
        # print(f"n: {n}, abs diff: {abs_diff}, mod_diff: {mod_diff}")

            operations += min(abs_diff, mod_diff)

    return operations


if __name__ == '__main__':
    nums = [3, 6, 9]
    # nums = [1, 2, 3, 4]
    # nums = [8]
    print(minimumOperations(nums))