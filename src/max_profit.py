def max_subarray_sum(prices):
    buy = min(prices)
    sell = max(prices[1:])
    return sell - buy

    # return max_seen - min_seen


if __name__ == '__main__':
    prices = [9, 1, 3, 6, 4, 8, 3, 5, 5]
    print(max_subarray_sum(prices))