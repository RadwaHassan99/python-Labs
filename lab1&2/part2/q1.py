def reduce_adjacent(nums):
    reduced = []
    for num in nums:
        if len(reduced) == 0 or num != reduced[-1]:
            reduced.append(num)
    return reduced


nums = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7]
reduced_nums = reduce_adjacent(nums)
print(reduced_nums)  # Output: [1, 2, 3, 4, 5, 6, 7]
