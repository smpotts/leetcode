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


# Write a function to find the longest common prefix string amongst an array of strings.
def longest_common_prefix(strs=["flowers", "flow"]):
    """
    :type strs: List[str]
    :rtype: str
    """

    # grab the first string to use to compare against the others
    first_str = strs[0]

    # loop through each character in the first one
    # build a string as we go until we hit a character that is not a match then break
    matched_results = []
    for word in strs[1:]:
        # loop through the length of the shorter word

        matched_letters = ""
        for i in range(min(len(word), len(first_str))):
            if first_str[i] == word[i]:
                matched_letters += word[i]
        matched_results.append(matched_letters)

    return min(matched_results, key=len)


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    # brackets = ['(', '']
    # loop through each character in the word
    for c in s:
        # if the letter is a bracket, add it to a stack or a map
        pass
    # loop through the stack
        # iterate on both ends?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # two_sum()
    # is_palindrome()
    longest_common_prefix()