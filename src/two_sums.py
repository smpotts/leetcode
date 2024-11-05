def two_sums(nums: list[int], target: int) -> list[int]:
    indices = [-1, -1]
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            # print(f"{nums[i]}, {nums[j]}")
            if nums[i] + nums[j] == target:
                indices = [i, j]
    return indices


if __name__ == "__main__":
    nums = [1, 4, 6, 10]
    target = 10
    print(two_sums(nums, target))