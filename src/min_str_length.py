def min_length(s):
    """
    :type s: str
    :rtype: int
    """
    str_len = len(s)
    i = 0
    while i < str_len - 1:
        letters = s[i] + s[i + 1]
        if letters in ("AB", "CD"):
            # s = s.replace(letters, '') INEFFICIENT
            s = s[:i] + s[i+2:]
            str_len = len(s)
            # reset the index
            i = 0
        else:
            i += 1

    if s in ("AB", "CD"):
        return 0
    else:
        return len(s)


def min_length_improved(n):
    """
    :type n: str
    :rtype: int
    """
    temp = []
    for ch in s:
        if temp and temp[-1] == 'A' and ch == 'B':
            temp.pop()
        elif temp and temp[-1] == 'C' and ch == 'D':
            temp.pop()
        else:
            temp += ch
    return len(temp)


if __name__ == '__main__':
    s = "ABFCACDB"
    s1 = "CCCCDDDD"
    s2 = "CCDDLLDW"
    print(min_length(s2))