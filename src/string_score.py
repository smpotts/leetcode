def score_of_string(s):
    """
    :type s: str
    :rtype: int
    """
    score = 0
    for char in range(len(s) - 1):
        score += abs(ord(s[char]) - ord(s[char + 1]))

    return score


if __name__ == '__main__':
    s = 'hello'
    print(score_of_string(s))

    t = 'zaz'
    print(score_of_string(t))
