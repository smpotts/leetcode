from collections import Counter


def min_swaps(s):
    """
    :type s: str
    :rtype: int
    """
    open = 0
    for i in s:
        if i == '[':
            open += 1
        elif i == ']' and open > 0:
            open -= 1

        print(f"i: {i}, open: {open}")

    # The variable open will contain the count of unmatched opening brackets that could not be paired with a closing
    # bracket. Since the string consists of equal numbers of [ and ], any unmatched closing brackets would have already
    # been accounted for when the open was decremented.

    # Each swap can resolve two unmatched brackets: one opening bracket and one closing bracket.
    # Thus, to determine the minimum number of swaps needed to balance the brackets, you take the total number of
    # unmatched opening brackets (open) and divide by 2
    return (open + 1) / 2


if __name__ == '__main__':
    s = "][]["
    s1 = "]]][[["
    s2 = '[]'
    min_swaps(s1)

