from collections import Counter


def check_inclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    len_s1 = len(s1)
    len_s2 = len(s2)

    # If s1 is longer than s2, it cannot be a permutation
    if len_s1 > len_s2:
        return False

    s1_count = Counter(s1)
    # Count characters in the first window of s2
    s2_count = Counter(s2[:len_s1])

    # Check if the counts are the same
    if s1_count == s2_count:
        return True

    for i in range(len_s1, len_s2):
        # Add the next character in s2 to the current window
        s2_count[s2[i]] += 1

        # Remove the character that is sliding out of the window
        s2_count[s2[i - len_s1]] -= 1

        # Remove the count from the dict if it becomes zero
        if s2_count[s2[i - len_s1]] == 0:
            del s2_count[s2[i - len_s1]]

        # Check if the counts match
        if s1_count == s2_count:
            return True

    return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    check_inclusion(s1, s2)