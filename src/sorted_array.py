def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique = set(nums)
    print(unique)
    return len(unique)


if __name__ == '__main__':
    nums = [1, 1, 2]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums))