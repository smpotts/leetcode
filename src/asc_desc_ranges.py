def solution(values, run_length):
    run_indices = []

    # iterate in groups of len(run_length) up to run_length - 1
    for i in range(0, len(values) - (run_length - 1)):
        block = values[i:i + run_length]
        print(block)

        # check that they are in asc or desc order, if so save the index
        if (block[0] + 1 == block[1] and block[0] + 2 == block[2]) \
                or (block[0] - 1 == block[1] and block[0] - 2 == block[2]):
            run_indices.append(i)

    # return the index list
    return run_indices


if __name__ == "__main__":
    solution([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7], 3)
