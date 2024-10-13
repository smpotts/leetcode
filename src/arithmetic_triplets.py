def arithmeticTriplets(nums: list[int], diff: int) -> int:
    triplet_list = []
    for i in range(0, len(nums)):
        triplet = [nums[i]]
        for j in range(i+1, len(nums)):
            print(f"i: {nums[i]}, j: {nums[j]}, max_triplet: {max(triplet)}")

            if nums[j] - nums[i] == diff or nums[j] - max(triplet) == diff:
                triplet.append(nums[j])

        print(triplet)
        if len(triplet) == 3:
            triplet_list.append(triplet)
    print(triplet_list)
    return len(triplet_list)


if __name__ == '__main__':
    nums = [1, 2, 4, 6, 7, 11, 12]
    diff = 5
    arithmeticTriplets(nums, 5)