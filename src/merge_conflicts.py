def has_merge_conflict(pull_requests)-> bool:
    for i in range(0, len(pull_requests)):
        first_pr = pull_requests[i]
        for j in range(i + 1, len(pull_requests)):
            second_pr = pull_requests[j]
            print(f"first_pr {first_pr}, second_pr: {second_pr}")

            # 1. first element between the first and second of the second pair
            if second_pr[0] <= first_pr[0] <= second_pr[1]:
                return True
            # 2. second element between the first and second of the second pair
            if second_pr[0] <= first_pr[1] <= second_pr[1]:
                return True
            # 3. second pair first element between first pair first and second
            if first_pr[0] <= second_pr[0] <= first_pr[1]:
                return True
            # 4. second pair second element between first and second
            if first_pr[0] <= second_pr[1] <= first_pr[1]:
                return True

    return False


if __name__ == '__main__':
    pull_reqs1 = [[5, 10], [15, 40], [25, 50]]
    pull_reqs2 = [[30, 40], [10, 20], [5, 8]]

    first_case_pr = [[5, 10], [4, 7]]
    second_case_pr = [[5, 10], [9, 12]]
    third_case_pr = [[5, 10], [6, 11]]
    fourth_case_pr = [[5, 10], [4, 8]]
    has_merge_conflict(pull_reqs2)
