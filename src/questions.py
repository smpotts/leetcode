"""
Leetcode Coding Practice Questions
"""


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
def two_sum(nums=[2, 7, 11, 15], target=9):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # double nested for loop through the nums
    # checking to see if i + j = target and if so adding index to an output array
    output_indexes = set()
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                output_indexes.add(i)
                output_indexes.add(j)
    return list(output_indexes)


# Given an integer x, return true if x is a palindrome, and false otherwise.
def is_palindrome(x=121):
    """
    :type x: int
    :rtype: bool
    """
    # hacky, but first check if negative and return false if it is
    if x < 0:
        return False

    stack = []
    # put the numbers into an array of characters
    for c in map(int, str(x)):
        stack.append(c)

    # once we have our stack pop them off and compare against original
    backwards = []
    for i in range(len(stack)):
        c = str(stack.pop())
        backwards.append(c)
    new_string = ''.join(backwards)

    if int(new_string) == x:
        return True
    return False


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums.
def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    uniques = set(nums)
    return len(uniques)


# def longest_common_prefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    two_sum()
    is_palindrome()
