def final_value_after_operations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    for op in operations:
        if '+' in op:
            x += 1
        elif '-' in op:
            x -= 1
    # print(x)
    return x


if __name__ == '__main__':
    # operations = ["--X", "X++", "X++"]
    operations = ["++X", "++X", "X++"]
    final_value_after_operations(operations)
